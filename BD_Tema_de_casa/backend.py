import datetime
import tkinter as tk
from tkinter import messagebox
import cx_Oracle

conn = None
cur = None
row = None
Table_names = []


def run_query(query: str):
    global conn, cur
    res = []
    try:
        cur = conn.cursor()
        cur.execute(query)
    except Exception as err:
        message = 'Error while running query: ' + str(err)
        tk.messagebox.showerror(title='Error', message=message)
        return []

    try:
        for x in cur:
            res.append(x)

    finally:

        # cur.execute('COMMIT')
        return res


def connection(name: str, password: str, host: str, port: str, service_name: str) -> list:
    global conn, cur
    try:
        # dsn_tns = cx_Oracle.makedsn('bd-dc.cs.tuiasi.ro', '1539', service_name='orcl')
        dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)
        conn = cx_Oracle.connect(user=name, password=password, dsn=dsn_tns)
        try:
            Table_Names = run_query('SELECT TABLE_NAME FROM USER_TABLES ORDER BY TABLE_NAME')
        except Exception as err:
            message = 'Error while getting table names: ' + str(err)
            tk.messagebox.showerror(title='Error', message=message)
    except Exception as err:
        message = "Error while creating the connection: "+ str(err)
        tk.messagebox.showerror(title='Error', message=message)
        exit(-1)
    else:
        print("\nConnection established.\n")

    return Table_Names


def close_connection():
    global conn, cur
    cur.close()
    conn.close()
    print("\nConnection closed.")


def convert_to_sql(value):
    if value is None:
        return 'NULL, '

    if type(value) == int or type(value) == float:
        return str(value) + ', '

    if type(value) == datetime.datetime:
        return 'TO_DATE(\'' + str(value.date()) + '\', \'RRRR-MM-DD\'), '

    if type(value) == str:
        if value.__contains__("SELECT"):
            return '(' + value + '), '
        else:
            return '\'' + value + '\', '

    return ', '


def select_from_table(table_name: str) -> list:
    global conn, cur, row
    try:
        row = run_query('SELECT * FROM ' + table_name)
        #for x in row:
        #    print(x)
    except Exception as err:
        message = 'Error while getting table values: '+ str(err)
        tk.messagebox.showerror(title='Error', message=message)
    return row


def insert_into_table(table_name: str, values: list):
    global conn, cur
    values_String = '('
    for x in values:
        values_String += convert_to_sql(x)

    values_String = values_String[:len(values_String) - 2] + ')'
    #print(table_name)
    #print('INSERT INTO ' + table_name + ' VALUES ' + values_String)

    try:
        run_query('INSERT INTO ' + table_name + ' VALUES ' + values_String)
    except Exception as err:
        message = 'Error while inserting into table: '+ str(err)
        tk.messagebox.showerror(title='Error', message=message)

    #cur.execute('COMMIT')


def insert_into_table_clienti(table_name: str, values: list):
    global conn, cur
    values_String = '('
    for x in values:
        values_String += convert_to_sql(x)

    values_String = values_String[:len(values_String) - 2] + ')'
    #print(table_name)
    #print('INSERT INTO ' + table_name + ' VALUES ' + values_String)

    try:
        cur.execute('SAVEPOINT TEMP')
        cur.execute('INSERT INTO ' + table_name + ' VALUES ' + values_String)
    except Exception as err:
        errors = 'WRONG'
        message = 'Error while inserting into table: '+ str(err)
        tk.messagebox.showerror(title='Error', message=message)
        return errors


def insert_into_table_adrese(table_name: str, values: list):
    global conn, cur
    values_String = '('
    for x in values:
        values_String += convert_to_sql(x)

    values_String = values_String[:len(values_String) - 2] + ')'
    #print(table_name)
    #print('INSERT INTO ' + table_name + ' VALUES ' + values_String)

    try:
        cur.execute('SAVEPOINT TEMP2')
        cur.execute('INSERT INTO ' + table_name + ' VALUES ' + values_String)
        if (len(select_from_table(Table_names[2][0])) > len(select_from_table(table_name))):
            cur.execute('ROLLBACK TO TEMP')
        elif (len(select_from_table(Table_names[2][0])) < len(select_from_table(table_name))):
            cur.execute('ROLLBACK TO TEMP2')
        else:
            cur.execute('COMMIT')
    except Exception as err:
        errors = 'WRONG'
        cur.execute('ROLLBACK TO TEMP')
        message = 'Error while inserting into table: '+ str(err)
        tk.messagebox.showerror(title='Error', message=message)
        return errors


def get_Column_names(table_name: str) -> list:
    global conn, cur
    try:
        list = run_query('SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = \'' + table_name + '\'')
    except Exception as err:
        message = 'Error while getting column names: '+ str(err)
        tk.messagebox.showerror(title='Error', message=message)

    return list


def update_table(table_name: str, column_name: str, values: str, condition: str):
    try:
        #conn.cursor().execute('UPDATE ' + table_name + ' SET ' + set + ' WHERE ' + where)
        cur.execute('UPDATE ' + table_name + ' SET ' + column_name + ' = \'' + values + '\' WHERE \'' + condition + '\'')
    except Exception as err:
        print('Error while updating table: ', err)

