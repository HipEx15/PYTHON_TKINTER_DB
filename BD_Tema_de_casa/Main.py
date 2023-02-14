import tkinter
from datetime import *
from tkinter import *
from tkinter import ttk, messagebox
import queue

import backend

main_menu = None
back = None
Adrese = None
Clienti = None
Comenzi = None
Memorie_ram = None
Placa_video = None
Procesor = None
Produse = None
Angajati = None
all_tabels = None
count = None
my_tree = None
savepoints = queue.Queue(maxsize=5)

def exit_button():
    backend.close_connection()
    exit(0)


def back_selection(menu):
    menu.pack_forget()
    show_tabels(menu)


def back_menu(menu):
    menu.pack_forget()
    menuinfo()


def menuinfo():
    global main_menu, back, Adrese, Clienti, Comenzi, Memorie_ram, Placa_video, Procesor, Produse, Angajati, all_tabels

    main_menu = Frame(root, bg="#34312D", width=900, height=600)

    main_menu.pack_forget()
    main_menu.pack(fill="both", expand=True)

    # Create the main menu
    menu_Label = Label(main_menu, text='Gestiunea activitatii unui magazin cu componente hardware', font=("Arial", 25),
                       bg="#34312D", fg="#D9C5B2")
    menu_Label.pack(pady=235)

    print_tabels = Button(main_menu, text="Afiseaza tabelele", font=("Arial", 15), bg="#34312D", fg="#D9C5B2", width=20,
                          height=2, command=lambda: show_tabels(main_menu))
    print_tabels.place(x=330, y=300)

    exitButton = Button(main_menu, text="Iesire", font=("Arial", 15), bg="#34312D", fg="#D9C5B2", width=20, height=2,
                        command=exit_button)
    exitButton.place(x=330, y=375)


def show_tabels(menu):
    global main_menu, back, Adrese, Clienti, Comenzi, Memorie_ram, Placa_video, Procesor, Produse, Angajati, all_tabels

    all_tabels = Frame(root, bg="#34312D", width=900, height=600)
    Adrese = Frame(root, bg="#34312D", width=900, height=600)
    Angajati = Frame(root, bg="#34312D", width=900, height=600)
    Clienti = Frame(root, bg="#34312D", width=900, height=600)
    Comenzi = Frame(root, bg="#34312D", width=900, height=600)
    Memorie_ram = Frame(root, bg="#34312D", width=900, height=600)
    Placa_video = Frame(root, bg="#34312D", width=900, height=600)
    Procesor = Frame(root, bg="#34312D", width=900, height=600)
    Produse = Frame(root, bg="#34312D", width=900, height=600)
    menu.pack_forget()
    all_tabels.pack(fill="both", expand=True)

    back = Button(all_tabels, text="Inapoi", font=("Arial", 15), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_menu(all_tabels))
    adrese = Button(all_tabels, text="Adrese", font=("Arial", 25), bg="#34312D", fg="#D9C5B2", command=adrese_info)
    angajati = Button(all_tabels, text="Angajati", font=("Arial", 25), bg="#34312D", fg="#D9C5B2",
                      command=angajati_info)
    clienti = Button(all_tabels, text="Clienti", font=("Arial", 25), bg="#34312D", fg="#D9C5B2", command=clienti_info)
    comenzi = Button(all_tabels, text="Comenzi", font=("Arial", 25), bg="#34312D", fg="#D9C5B2", command=comenzi_info)
    memorie_ram = Button(all_tabels, text="Memorie ram", font=("Arial", 25), bg="#34312D", fg="#D9C5B2",
                         command=memorie_ram_info)
    placa_video = Button(all_tabels, text="Placa video", font=("Arial", 25), bg="#34312D", fg="#D9C5B2",
                         command=placa_video_info)
    procesor = Button(all_tabels, text="Procesor", font=("Arial", 25), bg="#34312D", fg="#D9C5B2",
                      command=procesor_info)
    produse = Button(all_tabels, text="Produse", font=("Arial", 25), bg="#34312D", fg="#D9C5B2", command=produse_info)

    back.place(x=825, y=535)
    adrese.place(x=90, y=150, width=225, height=50)
    angajati.place(x=340, y=150, width=225, height=50)
    clienti.place(x=590, y=150, width=225, height=50)
    comenzi.place(x=90, y=250, width=225, height=50)
    memorie_ram.place(x=340, y=250, width=225, height=50)
    placa_video.place(x=590, y=250, width=225, height=50)
    procesor.place(x=90, y=350, width=225, height=50)
    produse.place(x=340, y=350, width=225, height=50)


def insert_into_adrese(window, tree, b, d, f, table, list):
    error = ''
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    #print(list)
    error = backend.insert_into_table_adrese(table, list)
    if (error == 'WRONG'):
        clienti_info()
    elif (error == None and len(backend.select_from_table(backend.Table_names[2][0])) == len(backend.select_from_table(table))):
        adrese_info()
    elif (len(backend.select_from_table(backend.Table_names[2][0])) < len(backend.select_from_table(table))):
        clienti_info()


def adrese_info():
    global my_tree
    all_tabels.forget()
    Adrese.pack(fill="both", expand=True)
    back = Button(Adrese, text="Inapoi", font=("Arial", 15), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Adrese))
    back.place(x=825, y=535)

    # adrese_Label = Label(Adrese, text='Adrese', font=("Arial", 25),
    #                     bg="#111111", fg="#D9C5B2")
    # adrese_Label.pack(pady=235)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Adrese)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[0][0])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0],
                          columns[5][0], columns[6][0])

    # print(my_tree)

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_ADRESA", anchor=W, width=85, stretch=NO)
    my_tree.column("STRADA", anchor=CENTER, width=225, stretch=NO)
    my_tree.column("ORAS", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("JUDET", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("TARA", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("COD_POSTAL", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("NUMAR_TELEFON", anchor=CENTER, width=150, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_ADRESA", text="COD_ADRESA", anchor=W)
    my_tree.heading("STRADA", text="STRADA", anchor=CENTER)
    my_tree.heading("ORAS", text="ORAS", anchor=CENTER)
    my_tree.heading("JUDET", text="JUDET", anchor=CENTER)
    my_tree.heading("TARA", text="TARA", anchor=CENTER)
    my_tree.heading("COD_POSTAL", text="COD_POSTAL", anchor=CENTER)
    my_tree.heading("NUMAR_TELEFON", text="NUMAR_TELEFON", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[0][0])

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Adrese, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    strada = Label(data_frame, text="Strada", background="#34312D", foreground="#E4D4C8")
    strada.grid(row=0, column=0, padx=10, pady=10)
    strada_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="strada")
    strada_entry.grid(row=0, column=1, padx=40, pady=10)

    oras = Label(data_frame, text="Oras", background="#34312D", foreground="#E4D4C8")
    oras.grid(row=0, column=2, padx=10, pady=10)
    oras_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="oras")
    oras_entry.grid(row=0, column=3, padx=65, pady=10)

    judet = Label(data_frame, text="Judet", background="#34312D", foreground="#E4D4C8")
    judet.grid(row=0, column=4, padx=10, pady=10)
    judet_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="judet")
    judet_entry.grid(row=0, column=5, padx=10, pady=10)

    tara = Label(data_frame, text="Tara", background="#34312D", foreground="#E4D4C8")
    tara.grid(row=1, column=0, padx=10, pady=10)
    tara_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="tara")
    tara_entry.grid(row=1, column=1, padx=10, pady=10)

    cd = Label(data_frame, text="Cod_postal", background="#34312D", foreground="#E4D4C8")
    cd.grid(row=1, column=2, padx=10, pady=10)
    cd_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="cd")
    cd_entry.grid(row=1, column=3, padx=10, pady=10)

    nrt = Label(data_frame, text="Numar_telefon", background="#34312D", foreground="#E4D4C8")
    nrt.grid(row=1, column=4, padx=10, pady=10)
    nrt_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="nrt")
    nrt_entry.grid(row=1, column=5, padx=10, pady=10)

    button_frame = LabelFrame(Adrese, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_adrese(Adrese, my_tree, data_frame, button_frame, tree_frame,
                                                           backend.Table_names[0][0],
                                                           [None, strada_entry.get(), oras_entry.get(),
                                                            judet_entry.get(), tara_entry.get(),
                                                            cd_entry.get(),
                                                            nrt_entry.get()]
                                                           ))

    add_button.grid(row=0, column=1, padx=10, pady=10)
    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_adrese(my_tree, strada_entry, oras_entry, judet_entry,
                                                                tara_entry, cd_entry, nrt_entry, id_entry)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_adrese(my_tree, id_entry, Adrese, data_frame, button_frame, tree_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza", command=lambda: cancel_update_adrese(Adrese, my_tree, data_frame, button_frame, tree_frame, strada_entry,
                                                                                             oras_entry, judet_entry,
                                                                                             tara_entry, cd_entry,
                                                                                             nrt_entry), background="#34312D", foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_adrese(e, data_frame))


def remove_record_adrese(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Adrese
                WHERE COD_ADRESA = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    adrese_info()



def cancel_update_adrese(window, tree, b, d, f, strada_entry,
                         oras_entry, judet_entry,
                         tara_entry, cd_entry,
                         nrt_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    strada_entry.delete(0, END)
    oras_entry.delete(0, END)
    judet_entry.delete(0, END)
    tara_entry.delete(0, END)
    cd_entry.delete(0, END)
    nrt_entry.delete(0, END)

    adrese_info()


def select_record_adrese(event, parent):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        # show a message

    for child in parent.winfo_children():
            if child.winfo_class() == "Entry":
                child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("strada").insert(0, record[1])
    parent.children.get("oras").insert(0, record[2])
    parent.children.get("judet").insert(0, record[3])
    parent.children.get("tara").insert(0, record[4])
    parent.children.get("cd").insert(0, record[5])
    parent.children.get("nrt").insert(0, record[6])


def update_record_adrese(my_tree, strada, oras, judet, tara, cd, nrt, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
        strada.get(), oras.get(), judet.get(), tara.get(), cd.get(), nrt.get()))

    try:
        backend.cur.execute("""UPDATE Adrese SET
            STRADA = :strada,
            ORAS = :oras,
            JUDET = :judet,
            TARA = :tara,
            COD_POSTAL = :cd,
            NUMAR_TELEFON = :nrt
    
            WHERE COD_ADRESA = :id""",
                  {
                      'strada': strada.get(),
                      'oras': oras.get(),
                      'judet': judet.get(),
                      'tara': tara.get(),
                      'cd': cd.get(),
                      'nrt': nrt.get(),
                      'id': id.get(),
                  })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)



def insert_into_angajati(window, tree, b, d, f, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    backend.insert_into_table(table, list)
    angajati_info()


def angajati_info():
    global my_tree
    all_tabels.forget()
    Angajati.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Angajati)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down,
                           selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[1][0])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0],
                          columns[5][0], columns[6][0], columns[7][0], columns[8][0])

    print(columns)

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_ANGAJAT", anchor=W, width=95, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=200, stretch=NO)
    my_tree.column("PRENUME", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("DATA_NASTERE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("NUMAR_TELEFON", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("EMAIL", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("DATA_ANGAJARE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("SALARIU", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("COMISION", anchor=CENTER, width=175, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_ANGAJAT", text="COD_ANGAJAT", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("PRENUME", text="PRENUME", anchor=CENTER)
    my_tree.heading("DATA_NASTERE", text="DATA_NASTERE", anchor=CENTER)
    my_tree.heading("NUMAR_TELEFON", text="NUMAR_TELEFON", anchor=CENTER)
    my_tree.heading("EMAIL", text="EMAIL", anchor=CENTER)
    my_tree.heading("DATA_ANGAJARE", text="DATA_ANGAJARE", anchor=CENTER)
    my_tree.heading("SALARIU", text="SALARIU", anchor=CENTER)
    my_tree.heading("COMISION", text="COMISION", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[1][0])
    #print(data)

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3].date(), record[4], record[5], record[6].date(), record[7],
                               record[8]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3].date(), record[4], record[5], record[6].date(), record[7],
                               record[8]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Angajati, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#34312D", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=40, pady=10)

    prenume = Label(data_frame, text="Prenume", background="#34312D", foreground="#E4D4C8")
    prenume.grid(row=0, column=2, padx=10, pady=10)
    prenume_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="prenume")
    prenume_entry.grid(row=0, column=3, padx=65, pady=10)

    data_nastere = Label(data_frame, text="Data_nastere", background="#34312D", foreground="#E4D4C8")
    data_nastere.grid(row=0, column=4, padx=10, pady=10)
    data_nastere_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                               textvariable=StringVar(Angajati, value=str(date.today())), name="data_nastere")
    data_nastere_entry.grid(row=0, column=5, padx=10, pady=10)

    numar_telefon = Label(data_frame, text="Numar_telefon", background="#34312D", foreground="#E4D4C8")
    numar_telefon.grid(row=1, column=0, padx=10, pady=10)
    numar_telefon_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="numar_telefon")
    numar_telefon_entry.grid(row=1, column=1, padx=10, pady=10)

    email = Label(data_frame, text="Email", background="#34312D", foreground="#E4D4C8")
    email.grid(row=1, column=2, padx=10, pady=10)
    email_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="email")
    email_entry.grid(row=1, column=3, padx=10, pady=10)

    data_angajare = Label(data_frame, text="Data_angajare", background="#34312D", foreground="#E4D4C8")
    data_angajare.grid(row=1, column=4, padx=10, pady=10)
    data_angajare_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                                textvariable=StringVar(Angajati, value=str(date.today())), name="data_angajare")
    data_angajare_entry.grid(row=1, column=5, padx=10, pady=10)

    salariu = Label(data_frame, text="Salariu", background="#34312D", foreground="#E4D4C8")
    salariu.grid(row=2, column=0, padx=10, pady=10)
    salariu_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                          textvariable=StringVar(Angajati, value="-1"), name="salariu")
    salariu_entry.grid(row=2, column=1, padx=10, pady=10)

    comision = Label(data_frame, text="Comision", background="#34312D", foreground="#E4D4C8")
    comision.grid(row=2, column=2, padx=10, pady=10)
    comision_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                           textvariable=StringVar(Angajati, value="-1"), name="comision")
    comision_entry.grid(row=2, column=3, padx=10, pady=10)

    button_frame = LabelFrame(Angajati, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    back = Button(Angajati, text="Inapoi", font=("Arial", 13), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Angajati))
    back.place(x=835, y=520)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_angajati(Angajati, my_tree, data_frame, button_frame, tree_frame,
                                                             backend.Table_names[1][0],
                                                             [None, nume_entry.get(), prenume_entry.get(),
                                                              datetime.strptime(data_nastere_entry.get(), '%Y-%m-%d'),
                                                              numar_telefon_entry.get(),
                                                              email_entry.get(),
                                                              datetime.strptime(data_angajare_entry.get(), '%Y-%m-%d'),
                                                              float(salariu_entry.get()), float(comision_entry.get())])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_angajati(my_tree, nume_entry, prenume_entry, data_nastere_entry,
                                                                  numar_telefon_entry, email_entry, data_angajare_entry, salariu_entry
                                                                  , comision_entry, id_entry)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_angajati(my_tree, id_entry, Angajati, data_frame,
                                                                  button_frame, tree_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_angajati(Angajati, my_tree, data_frame, button_frame, tree_frame,
                                                                  nume_entry, prenume_entry, data_nastere_entry,
                                                                  numar_telefon_entry, email_entry, data_angajare_entry,
                                                                  salariu_entry
                                                                  , comision_entry), background="#34312D",
                           foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_angajati(e, data_frame))

def remove_record_angajati(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Angajati
                WHERE COD_ANGAJAT = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    angajati_info()

def cancel_update_angajati(window, tree, b, d, f, nume_entry, prenume_entry, data_nastere_entry,
                                                                  numar_telefon_entry, email_entry, data_angajare_entry,
                                                                  salariu_entry
                                                                  , comision_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()

    nume_entry.delete(0, END)
    prenume_entry.delete(0, END)
    data_nastere_entry.delete(0, END)
    numar_telefon_entry.delete(0, END)
    email_entry.delete(0, END)
    data_angajare_entry.delete(0, END)
    salariu_entry.delete(0, END)
    comision_entry.delete(0, END)

    angajati_info()


def select_record_angajati(event, parent):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        # show a message
    #print(record)

    for child in parent.winfo_children():
            if child.winfo_class() == "Entry":
                child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("prenume").insert(0, record[2])
    parent.children.get("data_nastere").insert(0, record[3])
    parent.children.get("numar_telefon").insert(0, record[4])
    parent.children.get("email").insert(0, record[5])
    parent.children.get("data_angajare").insert(0, record[6])
    parent.children.get("salariu").insert(0, record[7])
    parent.children.get("comision").insert(0, record[8])


def update_record_angajati(my_tree, nume, prenume, data_nastere, numar_telefon, email, data_angajare, salariu, comision, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
        nume.get(), prenume.get(), datetime.strptime(data_nastere.get(), '%Y-%m-%d').date(), numar_telefon.get(), email.get(), datetime.strptime(data_angajare.get(), '%Y-%m-%d').date(), salariu.get(), comision.get()))

    try:
        backend.cur.execute("""UPDATE Angajati SET
            NUME = :nume,
            PRENUME = :prenume,
            DATA_NASTERE = :data_nastere,
            NUMAR_TELEFON = :numar_telefon,
            EMAIL = :email,
            DATA_ANGAJARE = :data_angajare,
            SALARIU = :salariu,
            COMISION = :comision
    
            WHERE COD_ANGAJAT = :id""",
                  {
                      'nume': nume.get(),
                      'prenume': prenume.get(),
                      'data_nastere': datetime.strptime(data_nastere.get(), '%Y-%m-%d').date(),
                      'numar_telefon': numar_telefon.get(),
                      'email': email.get(),
                      'data_angajare': datetime.strptime(data_angajare.get(), '%Y-%m-%d').date(),
                      'salariu': salariu.get(),
                      'comision': comision.get(),
                      'id': id.get()
                  })

        backend.cur.execute(
            """
        SELECT cpu_usage_percent =: cpu_up FROM cpu =: nume_tabela
        WHERE cpu_date=:data_cpu = (select to_char(sysdate - 2, 'DD-MON-YYYY') from dual)
        AND cpu_time=:ora_cpu between (select to_char(sysdate, 'HH24:MI:SS') from dual) AND 23:59:59
        OR cpu_date=:data_cpu = (select to_char(sysdate, 'DD-MON-YYYY') from dual)
        AND cpu_time=:ora_cpu < (select to_char(sysdate, 'HH24:MI:SS') from dual)
        OR cpu_date=:data_cpu between (select to_char(sysdate - 2, 'DD-MON-YYYY') from dual) AND (select to_char(sysdate, 'DD-MON-YYYY') from dual);""",
                            {
                                'cpu_up': data,
                                'nume_tabela': table,
                                'data_cpu': date_column,
                                'ora_cpu': time_column
                            });
        
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

def insert_into_clienti(window, tree, b, d, f, table, list):
    error = ''
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    error = backend.insert_into_table_clienti(table, list)
    if(error == 'WRONG'):
        clienti_info()
    elif(error == None):
        adrese_info()

def clienti_info():
    global my_tree
    all_tabels.forget()
    Clienti.pack(fill="both", expand=True)
    back = Button(Clienti, text="Inapoi", font=("Arial", 15), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Clienti))
    back.place(x=825, y=535)

    # clienti_Label = Label(Clienti, text='Clienti', font=("Arial", 25),
    #                      bg="#111111", fg="#D9C5B2")
    # clienti_Label.pack(pady=235)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Clienti)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[2][0])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0])

    # print(my_tree)

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_CLIENT", anchor=W, width=100, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("PRENUME", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("EMAIL", anchor=CENTER, width=250, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_CLIENT", text="COD_CLIENT", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("PRENUME", text="PRENUME", anchor=CENTER)
    my_tree.heading("EMAIL", text="EMAIL", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[2][0])

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Clienti, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#34312D", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=40, pady=10)

    prenume = Label(data_frame, text="Prenume", background="#34312D", foreground="#E4D4C8")
    prenume.grid(row=0, column=2, padx=10, pady=10)
    prenume_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="prenume")
    prenume_entry.grid(row=0, column=3, padx=65, pady=10)

    email = Label(data_frame, text="Email", background="#34312D", foreground="#E4D4C8")
    email.grid(row=0, column=4, padx=10, pady=10)
    email_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="email")
    email_entry.grid(row=0, column=5, padx=10, pady=10)

    button_frame = LabelFrame(Clienti, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_clienti(Clienti, my_tree, data_frame, button_frame, tree_frame,
                                                            backend.Table_names[2][0],
                                                            [None, nume_entry.get(), prenume_entry.get(),
                                                             email_entry.get()])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_clienti(my_tree, nume_entry, prenume_entry, email_entry, id_entry)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_clienti(my_tree, id_entry, Clienti, data_frame,
                                                                 button_frame, tree_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_clienti(Clienti, my_tree, data_frame, button_frame, tree_frame,
                                                                 nume_entry, prenume_entry, email_entry), background="#34312D", foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_clienti(e, data_frame))

def remove_record_clienti(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Clienti
                WHERE COD_CLIENT = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    clienti_info()

def cancel_update_clienti(window, tree, b, d, f, nume_entry, prenume_entry, email_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    nume_entry.delete(0, END)
    prenume_entry.delete(0, END)
    email_entry.delete(0, END)

    clienti_info()


def select_record_clienti(event, parent):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        # show a message
    #print(record)

    for child in parent.winfo_children():
            if child.winfo_class() == "Entry":
                child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("prenume").insert(0, record[2])
    parent.children.get("email").insert(0, record[3])


def update_record_clienti(my_tree, nume, prenume, email, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
        nume.get(), prenume.get(), email.get()))

    try:
        backend.cur.execute("""UPDATE Clienti SET
            NUME = :nume,
            PRENUME = :prenume,
            EMAIL = :email
    
            WHERE COD_CLIENT = :id""",
                  {
                      'nume': nume.get(),
                      'prenume': prenume.get(),
                      'email': email.get(),
                      'id': id.get()
                  })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

def insert_into_comanda(window, tree, b, d, f, s, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    backend.insert_into_table(table, list)
    comenzi_info()


def update_comanda(my_tree, data_cumpararii_entry, modalitate_de_plata_entry, clicked_clienti, clicked_angajati, clicked_adrese, id_entry, window, b, d, f, s):
    update_record_comenzi(my_tree, data_cumpararii_entry, modalitate_de_plata_entry, clicked_clienti, clicked_angajati,
                          clicked_adrese, id_entry)
    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    comenzi_info()


def comenzi_info():
    global my_tree

    all_tabels.forget()
    Comenzi.pack(fill="both", expand=True)

    # comenzi_Label = Label(Comenzi, text='Comenzi', font=("Arial", 25),
    #                      bg="#111111", fg="#D9C5B2")
    # comenzi_Label.pack(pady=235)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Comenzi)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[3][0])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0],
                          columns[5][0])

    # print(my_tree)

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_COMANDA", anchor=W, width=105, stretch=NO)
    my_tree.column("DATA_CUMPARARII", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("MODALITATE_DE_PLATA", anchor=CENTER, width=145, stretch=NO)
    my_tree.column("CLIENTI_COD_CLIENT", anchor=CENTER, width=145, stretch=NO)
    my_tree.column("ANGAJATI_COD_ANGAJAT", anchor=CENTER, width=145, stretch=NO)
    my_tree.column("ADRESE_COD_ADRESA", anchor=CENTER, width=145, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_COMANDA", text="COD_COMANDA", anchor=W)
    my_tree.heading("DATA_CUMPARARII", text="DATA_CUMPARARII", anchor=CENTER)
    my_tree.heading("MODALITATE_DE_PLATA", text="MODALITATE_DE_PLATA", anchor=CENTER)
    my_tree.heading("CLIENTI_COD_CLIENT", text="CLIENTI_COD_CLIENT", anchor=CENTER)
    my_tree.heading("ANGAJATI_COD_ANGAJAT", text="ANGAJATI_COD_ANGAJAT", anchor=CENTER)
    my_tree.heading("ADRESE_COD_ADRESA", text="ADRESE_COD_ADRESA", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[3][0])

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1].date(), record[2], record[3], record[4], record[5]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1].date(), record[2], record[3], record[4], record[5]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Comenzi, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    data_cumpararii = Label(data_frame, text="Data_cumpararii", background="#34312D", foreground="#E4D4C8")
    data_cumpararii.grid(row=0, column=0, padx=10, pady=10)
    data_cumpararii_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                                  textvariable=StringVar(Comenzi, value=str(date.today())), name="data_cumpararii")
    data_cumpararii_entry.grid(row=0, column=1, padx=40, pady=10)

    modalitate_de_plata = Label(data_frame, text="Modalitate_de_plata", background="#34312D", foreground="#E4D4C8")
    modalitate_de_plata.grid(row=0, column=2, padx=10, pady=10)
    modalitate_de_plata_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="modalitate_de_plata")
    modalitate_de_plata_entry.grid(row=0, column=3, padx=65, pady=10)

    select_frame = LabelFrame(Comenzi, text="Alegeti datele:", background="#34312D", foreground="#E4D4C8")
    select_frame.pack(pady=0, padx=0, fill='x')

    tabela_clienti = backend.select_from_table(backend.Table_names[2][0])
    tabela_angajati = backend.select_from_table(backend.Table_names[1][0])
    tabela_adrese = backend.select_from_table(backend.Table_names[0][0])

    clicked_clienti = StringVar(Comenzi)
    clicked_clienti.set(tabela_clienti[0])
    alege_client = Label(select_frame, text="Alegeti clientul", background="#34312D", foreground="#E4D4C8")
    alege_client.grid(row=0, column=0)
    drop_clienti = OptionMenu(select_frame, clicked_clienti, *tabela_clienti)
    drop_clienti.configure(background="#34312D", foreground="#E4D4C8", activebackground="#34312D", activeforeground="#E4D4C8", highlightthickness=0)
    drop_clienti.grid(row=0, column=1, padx=0, pady=1)
    #print(clicked_clienti.get().replace(',','     ')[1:4])
    #print(clicked_clienti.get()[1])

    clicked_angajati = StringVar(Comenzi)
    clicked_angajati.set(tabela_angajati[0])
    alege_angajat = Label(select_frame, text="Alegeti angajatul", background="#34312D", foreground="#E4D4C8")
    alege_angajat.grid(row=1, column=0)
    drop_angajati = OptionMenu(select_frame, clicked_angajati, *tabela_angajati)
    drop_angajati.configure(background="#34312D", foreground="#E4D4C8", activebackground="#34312D",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_angajati.grid(row=1, column=1, padx=50, pady=0)

    clicked_adrese = StringVar(Comenzi)
    clicked_adrese.set(tabela_adrese[0])
    alege_adresa = Label(select_frame, text="Alegeti adresa", background="#34312D", foreground="#E4D4C8")
    alege_adresa.grid(row=2, column=0)
    drop_adrese = OptionMenu(select_frame, clicked_adrese, *tabela_adrese)
    drop_adrese.configure(background="#34312D", foreground="#E4D4C8", activebackground="#34312D",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_adrese.grid(row=2, column=1,padx=0, pady=1)
    #print(clicked_clienti.get()[1])

    button_frame = LabelFrame(Comenzi, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_comanda(Comenzi, my_tree, data_frame, button_frame, tree_frame, select_frame,
                                                            backend.Table_names[3][0],
                                                            [None,
                                                             datetime.strptime(data_cumpararii_entry.get(), '%Y-%m-%d'),
                                                             modalitate_de_plata_entry.get(),
                                                             int(clicked_clienti.get().replace(',','     ')[1:4]),
                                                             int(clicked_angajati.get().replace(',','     ')[1:4]),
                                                             int(clicked_adrese.get().replace(',','     ')[1:4])])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    #command_button = Button(button_frame, text="Comanda",
    #                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",

    back = Button(Comenzi, text="Inapoi", font=("Arial", 15), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Comenzi))
    back.place(x=825, y=535)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_comanda(my_tree, data_cumpararii_entry, modalitate_de_plata_entry, clicked_clienti, clicked_angajati, clicked_adrese, id_entry,
                                                                Comenzi, data_frame, button_frame, tree_frame, select_frame)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)
    #foreign_key = [tabela_clienti[0][0], tabela_angajati[0][0], tabela_adrese[0][0]]
    #print(foreign_key)
    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_comenzi(my_tree, id_entry, Comenzi, data_frame,
                                                                 button_frame, tree_frame, select_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_comenzi(Comenzi, my_tree, data_frame, button_frame, tree_frame, select_frame,
                                                                 data_cumpararii_entry, modalitate_de_plata_entry),
                           background="#34312D", foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_comenzi(e, data_frame, clicked_clienti, clicked_angajati, clicked_adrese, tabela_clienti, tabela_angajati, tabela_adrese))

def remove_record_comenzi(my_tree, id, window, b, d, f, s):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Comenzi
                WHERE COD_COMANDA = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    comenzi_info()

def cancel_update_comenzi(window, tree, b, d, f, s, data_cumpararii_entry, modalitate_de_plata_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    data_cumpararii_entry.delete(0, END)
    modalitate_de_plata_entry.delete(0, END)

    comenzi_info()


def select_record_comenzi(event, parent, clienti, angajati, adrese, tc, ta, ta2):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        #print(record[3], record[4], record[5])
        # show a message
    #print(record)

    for child in parent.winfo_children():
            if child.winfo_class() == "Entry":
                child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("data_cumpararii").insert(0, record[1])
    parent.children.get("modalitate_de_plata").insert(0, record[2])
    clienti.set(tc[record[3]-1])
    angajati.set(ta[record[4]-1])
    adrese.set(ta2[record[5]-1])


def update_record_comenzi(my_tree, data_cumpararii_entry, modalitate_de_plata_entry, clicked_clienti, clicked_angajati, clicked_adrese, id_entry):
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    try:
        backend.cur.execute("""UPDATE COMENZI SET
            DATA_CUMPARARII = :data_cumpararii,
            MODALITATE_DE_PLATA = :modalitate_de_plata,
            CLIENTI_COD_CLIENT = :ccc,
            ANGAJATI_COD_ANGAJAT = :aca,
            ADRESE_COD_ADRESA = :adrc
    
            WHERE COD_COMANDA = :id""",
                  {
                      'data_cumpararii': datetime.strptime(data_cumpararii_entry.get(), '%Y-%m-%d').date(),
                      'modalitate_de_plata': modalitate_de_plata_entry.get(),
                      'ccc': int(clicked_clienti.get().replace(',','     ')[1:4]),
                      'aca': int(clicked_angajati.get().replace(',','     ')[1:4]),
                      'adrc': int(clicked_adrese.get().replace(',','     ')[1:4]),
                      'id': id_entry.get()
                  })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_memorie(window, tree, b, d, f, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    backend.insert_into_table(table, list)
    memorie_ram_info()


def memorie_ram_info():
    global my_tree
    all_tabels.forget()
    Memorie_ram.pack(fill="both", expand=True)

    # memorie_ram_Label = Label(Memorie_ram, text='Memorie ram', font=("Arial", 25),
    #                          bg="#111111", fg="#D9C5B2")
    # memorie_ram_Label.pack(pady=235)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Memorie_ram)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down,
                           selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[4][0])
    # print(columns)
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0],
                          columns[5][0], columns[6][0], columns[7][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_RAM", anchor=W, width=70, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("TIP_MEMORIE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("CAPACITATE_MEMORIE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("FRECVENTA", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("STANDARD", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("RADIATOR", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("PRET", anchor=CENTER, width=175, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_RAM", text="COD_RAM", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("TIP_MEMORIE", text="TIP_MEMORIE", anchor=CENTER)
    my_tree.heading("CAPACITATE_MEMORIE", text="CAPACITATE_MEMORIE", anchor=CENTER)
    my_tree.heading("FRECVENTA", text="FRECVENTA", anchor=CENTER)
    my_tree.heading("STANDARD", text="STANDARD", anchor=CENTER)
    my_tree.heading("RADIATOR", text="RADIATOR", anchor=CENTER)
    my_tree.heading("PRET", text="PRET", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[4][0])
    # print(data)

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Memorie_ram, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#34312D", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=40, pady=10)

    tip_memorie = Label(data_frame, text="Tip_memorie", background="#34312D", foreground="#E4D4C8")
    tip_memorie.grid(row=0, column=2, padx=10, pady=10)
    tip_memorie_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name= "tip_memorie")
    tip_memorie_entry.grid(row=0, column=3, padx=65, pady=10)

    capacitate_memorie = Label(data_frame, text="Capacitate_memorie", background="#34312D", foreground="#E4D4C8")
    capacitate_memorie.grid(row=0, column=4, padx=0, pady=0)
    capacitate_memorie_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                                     textvariable=StringVar(Memorie_ram, value="-1"), name="capacitate_memorie")
    capacitate_memorie_entry.grid(row=0, column=5, padx=0, pady=0)

    frecventa = Label(data_frame, text="Frecventa", background="#34312D", foreground="#E4D4C8")
    frecventa.grid(row=1, column=0, padx=10, pady=10)
    frecventa_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                            textvariable=StringVar(Memorie_ram, value="-1"), name="frecventa")
    frecventa_entry.grid(row=1, column=1, padx=10, pady=10)

    standard = Label(data_frame, text="Standard", background="#34312D", foreground="#E4D4C8")
    standard.grid(row=1, column=2, padx=10, pady=10)
    standard_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="standard")
    standard_entry.grid(row=1, column=3, padx=10, pady=10)

    radiator = Label(data_frame, text="Radiator", background="#34312D", foreground="#E4D4C8")
    radiator.grid(row=1, column=4, padx=10, pady=10)
    radiator_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="radiator")
    radiator_entry.grid(row=1, column=5, padx=10, pady=10)

    pret = Label(data_frame, text="Pret", background="#34312D", foreground="#E4D4C8")
    pret.grid(row=2, column=0, padx=10, pady=10)
    pret_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                       textvariable=StringVar(Memorie_ram, value="-1"), name="pret")
    pret_entry.grid(row=2, column=1, padx=10, pady=10)

    button_frame = LabelFrame(Memorie_ram, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    back = Button(Memorie_ram, text="Inapoi", font=("Arial", 13), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Memorie_ram))
    back.place(x=835, y=520)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_memorie(Memorie_ram, my_tree, data_frame, button_frame, tree_frame,
                                                            backend.Table_names[4][0],
                                                            [None, nume_entry.get(), tip_memorie_entry.get(),
                                                             int(capacitate_memorie_entry.get()),
                                                             float(frecventa_entry.get()),
                                                             standard_entry.get(),
                                                             radiator_entry.get(),
                                                             float(pret_entry.get())]
                                                            ))

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_memorie(my_tree, nume_entry, tip_memorie_entry, capacitate_memorie_entry, frecventa_entry,
                                                                 standard_entry, radiator_entry, pret_entry, id_entry)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_memorie(my_tree, id_entry, Memorie_ram, data_frame,
                                                                 button_frame, tree_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_memorie(Memorie_ram, my_tree, data_frame, button_frame, tree_frame,
                                                                 nume_entry, tip_memorie_entry,
                                                                 capacitate_memorie_entry, frecventa_entry,
                                                                 standard_entry, radiator_entry, pret_entry),
                           background="#34312D", foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_memorie(e, data_frame))

def remove_record_memorie(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Memorie_ram
                WHERE COD_RAM = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    memorie_ram_info()

def cancel_update_memorie(window, tree, b, d, f, nume_entry, tip_memorie_entry,
                                                 capacitate_memorie_entry, frecventa_entry,
                                                 standard_entry, radiator_entry, pret_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    nume_entry.delete(0, END)
    tip_memorie_entry.delete(0, END)
    capacitate_memorie_entry.delete(0, END)
    frecventa_entry.delete(0, END)
    standard_entry.delete(0, END)
    radiator_entry.delete(0, END)
    pret_entry.delete(0, END)

    memorie_ram_info()

def select_record_memorie(event, parent):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        # show a message
    #print(record)

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("tip_memorie").insert(0, record[2])
    parent.children.get("capacitate_memorie").insert(0, record[3])
    parent.children.get("frecventa").insert(0, record[4])
    parent.children.get("standard").insert(0, record[5])
    parent.children.get("radiator").insert(0, record[6])
    parent.children.get("pret").insert(0, record[7])


def update_record_memorie(my_tree, nume, tip_memorie, capacitate_memorie, frecventa, standard, radiator, pret, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
                                            nume.get(), tip_memorie.get(), capacitate_memorie.get(), frecventa.get(),
                                            standard.get(), radiator.get(), pret.get()))
    #print(frecventa.get())
    try:
        backend.cur.execute("""UPDATE Memorie_ram SET
                NUME = :nume,
                TIP_MEMORIE = :tip_memorie,
                CAPACITATE_MEMORIE = :capacitate_memorie,
                FRECVENTA = :frecventa,
                STANDARD = :standard,
                RADIATOR = :radiator,
                PRET = :pret
    
                WHERE COD_RAM = :id""",
                            {
                                'nume': nume.get(),
                                'tip_memorie': tip_memorie.get(),
                                'capacitate_memorie': int(capacitate_memorie.get()),
                                'frecventa': float(frecventa.get()),
                                'standard': standard.get(),
                                'radiator': radiator.get(),
                                'pret': float(pret.get()),
                                'id': id.get()
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_placa(window, tree, b, d, f, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    backend.insert_into_table(table, list)
    placa_video_info()


def placa_video_info():
    global my_tree
    all_tabels.forget()
    Placa_video.pack(fill="both", expand=True)
    back = Button(Placa_video, text="Inapoi", font=("Arial", 15), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Placa_video))
    back.place(x=825, y=535)

    # placa_video_Label = Label(Placa_video, text='Placa video', font=("Arial", 25),
    #                          bg="#111111", fg="#D9C5B2")
    # placa_video_Label.pack(pady=235)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Placa_video)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down,
                           selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[5][0])
    # print(columns)
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0],
                          columns[5][0], columns[6][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_PLACA_VIDEO", anchor=W, width=115, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=225, stretch=NO)
    my_tree.column("TIP_MEMORIE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("CAPACITATE_MEMORIE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("FRECVENTA", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("PUTERE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("PRET", anchor=CENTER, width=175, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_PLACA_VIDEO", text="COD_PLACA_VIDEO", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("TIP_MEMORIE", text="TIP_MEMORIE", anchor=CENTER)
    my_tree.heading("CAPACITATE_MEMORIE", text="CAPACITATE_MEMORIE", anchor=CENTER)
    my_tree.heading("FRECVENTA", text="FRECVENTA", anchor=CENTER)
    my_tree.heading("PUTERE", text="PUTERE", anchor=CENTER)
    my_tree.heading("PRET", text="PRET", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[5][0])
    # print(data)

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Placa_video, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#34312D", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=40, pady=10)

    tip_memorie = Label(data_frame, text="Tip_memorie", background="#34312D", foreground="#E4D4C8")
    tip_memorie.grid(row=0, column=2, padx=10, pady=10)
    tip_memorie_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="tip_memorie")
    tip_memorie_entry.grid(row=0, column=3, padx=65, pady=10)

    capacitate_memorie = Label(data_frame, text="Capacitate_memorie", background="#34312D", foreground="#E4D4C8")
    capacitate_memorie.grid(row=0, column=4, padx=0, pady=0)
    capacitate_memorie_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                                     textvariable=StringVar(Placa_video, value="-1"), name="capacitate_memorie")
    capacitate_memorie_entry.grid(row=0, column=5, padx=0, pady=0)

    frecventa = Label(data_frame, text="Frecventa", background="#34312D", foreground="#E4D4C8")
    frecventa.grid(row=1, column=0, padx=10, pady=10)
    frecventa_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                            textvariable=StringVar(Placa_video, value="-1"), name="frecventa")
    frecventa_entry.grid(row=1, column=1, padx=10, pady=10)

    putere = Label(data_frame, text="Putere", background="#34312D", foreground="#E4D4C8")
    putere.grid(row=1, column=2, padx=10, pady=10)
    putere_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8"
                        ,textvariable = StringVar(Placa_video, value="-1"), name="putere")
    putere_entry.grid(row=1, column=3, padx=10, pady=10)

    pret = Label(data_frame, text="Pret", background="#34312D", foreground="#E4D4C8")
    pret.grid(row=1, column=4, padx=10, pady=10)
    pret_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                       textvariable=StringVar(Placa_video, value="-1"), name="pret")
    pret_entry.grid(row=1, column=5, padx=10, pady=10)

    button_frame = LabelFrame(Placa_video, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_placa(Placa_video, my_tree, data_frame, button_frame, tree_frame,
                                                          backend.Table_names[5][0],
                                                          [None, nume_entry.get(), tip_memorie_entry.get(),
                                                           int(capacitate_memorie_entry.get()),
                                                           float(frecventa_entry.get()), float(putere_entry.get()),
                                                           float(pret_entry.get())]
                                                          ))

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_video(my_tree, nume_entry, tip_memorie_entry,
                                                               capacitate_memorie_entry, frecventa_entry,
                                                               putere_entry, pret_entry, id_entry)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_video(my_tree, id_entry, Placa_video, data_frame,
                                                               button_frame, tree_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_video(Placa_video, my_tree, data_frame, button_frame, tree_frame,
                                                               nume_entry, tip_memorie_entry,
                                                               capacitate_memorie_entry, frecventa_entry,
                                                               putere_entry, pret_entry),
                           background="#34312D", foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_video(e, data_frame))


def remove_record_video(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Placa_video
                WHERE COD_PLACA_VIDEO = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    placa_video_info()

def cancel_update_video(window, tree, b, d, f, nume_entry, tip_memorie_entry,
                                                                capacitate_memorie_entry, frecventa_entry,
                                                                putere_entry, pret_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    nume_entry.delete(0, END)
    tip_memorie_entry.delete(0, END)
    capacitate_memorie_entry.delete(0, END)
    frecventa_entry.delete(0, END)
    putere_entry.delete(0, END)
    pret_entry.delete(0, END)

    placa_video_info()

def select_record_video(event, parent):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        # show a message
    #print(record)

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("tip_memorie").insert(0, record[2])
    parent.children.get("capacitate_memorie").insert(0, record[3])
    parent.children.get("frecventa").insert(0, record[4])
    parent.children.get("putere").insert(0, record[5])
    parent.children.get("pret").insert(0, record[6])


def update_record_video(my_tree, nume, tip_memorie, capacitate_memorie, frecventa, putere, pret, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
                                            nume.get(), tip_memorie.get(), capacitate_memorie.get(), frecventa.get(),
                                            putere.get(), pret.get()))
    #print(frecventa.get())
    try:
        backend.cur.execute("""UPDATE Placa_video SET
                    NUME = :nume,
                    TIP_MEMORIE = :tip_memorie,
                    CAPACITATE_MEMORIE = :capacitate_memorie,
                    FRECVENTA = :frecventa,
                    PUTERE = :putere,
                    PRET = :pret
    
                    WHERE COD_PLACA_VIDEO = :id""",
                            {
                                'nume': nume.get(),
                                'tip_memorie': tip_memorie.get(),
                                'capacitate_memorie': int(capacitate_memorie.get()),
                                'frecventa': float(frecventa.get()),
                                'putere': float(putere.get()),
                                'pret': float(pret.get()),
                                'id': id.get()
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_procesor(window, tree, b, d, f, table, list):
    #print(list)
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    backend.insert_into_table(table, list)
    procesor_info()


def procesor_info():
    global my_tree
    all_tabels.forget()
    Procesor.pack(fill="both", expand=True)
    back = Button(Procesor, text="Inapoi", font=("Arial", 15), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Procesor))
    back.place(x=825, y=535)

    # procesor_Label = Label(Procesor, text='Procesor', font=("Arial", 25),
    #                       bg="#111111", fg="#D9C5B2")
    # procesor_Label.pack(pady=235)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Procesor)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down,
                           selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[6][0])
    # print(columns)
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0],
                          columns[5][0], columns[6][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_PROCESOR", anchor=W, width=100, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=225, stretch=NO)
    my_tree.column("NUCLEE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("THREADURI", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("FRECVENTA", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("PUTERE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("PRET", anchor=CENTER, width=175, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_PROCESOR", text="COD_PROCESOR", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("NUCLEE", text="NUCLEE", anchor=CENTER)
    my_tree.heading("THREADURI", text="THREADURI", anchor=CENTER)
    my_tree.heading("FRECVENTA", text="FRECVENTA", anchor=CENTER)
    my_tree.heading("PUTERE", text="PUTERE", anchor=CENTER)
    my_tree.heading("PRET", text="PRET", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[6][0])
    # print(data)

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Procesor, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#34312D", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=40, pady=10)

    nuclee = Label(data_frame, text="Nuclee", background="#34312D", foreground="#E4D4C8")
    nuclee.grid(row=0, column=2, padx=10, pady=10)
    nuclee_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                         textvariable=StringVar(Procesor, value="-1"), name="nuclee")
    nuclee_entry.grid(row=0, column=3, padx=65, pady=10)

    threaduri = Label(data_frame, text="Threaduri", background="#34312D", foreground="#E4D4C8")
    threaduri.grid(row=0, column=4, padx=0, pady=0)
    threaduri_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                            textvariable=StringVar(Procesor, value="-1"), name="threaduri")
    threaduri_entry.grid(row=0, column=5, padx=0, pady=0)

    frecventa = Label(data_frame, text="Frecventa", background="#34312D", foreground="#E4D4C8")
    frecventa.grid(row=1, column=0, padx=10, pady=10)
    frecventa_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                            textvariable=StringVar(Procesor, value="-1"), name="frecventa")
    frecventa_entry.grid(row=1, column=1, padx=10, pady=10)

    putere = Label(data_frame, text="Putere", background="#34312D", foreground="#E4D4C8")
    putere.grid(row=1, column=2, padx=10, pady=10)
    putere_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                         textvariable=StringVar(Procesor, value="-1"), name="putere")
    putere_entry.grid(row=1, column=3, padx=10, pady=10)

    pret = Label(data_frame, text="Pret", background="#34312D", foreground="#E4D4C8")
    pret.grid(row=1, column=4, padx=10, pady=10)
    pret_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8",
                       textvariable=StringVar(Procesor, value="-1"), name="pret")
    pret_entry.grid(row=1, column=5, padx=10, pady=10)

    button_frame = LabelFrame(Procesor, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_procesor(Procesor, my_tree, data_frame, button_frame, tree_frame,
                                                             backend.Table_names[6][0],
                                                             [None, nume_entry.get(), int(nuclee_entry.get()),
                                                              int(threaduri_entry.get()), float(frecventa_entry.get()),
                                                              float(putere_entry.get()), float(pret_entry.get())]
                                                             ))

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_procesor(my_tree, nume_entry, nuclee_entry, threaduri_entry,
                                                                  frecventa_entry, putere_entry, pret_entry, id_entry)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_procesor(my_tree, id_entry, Procesor, data_frame,
                                                                  button_frame, tree_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_procesor(Procesor, my_tree, data_frame, button_frame, tree_frame,
                                                                  nume_entry, nuclee_entry, threaduri_entry,
                                                                  frecventa_entry, putere_entry, pret_entry),
                           background="#34312D", foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_procesor(e, data_frame))


def remove_record_procesor(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Procesor
                WHERE COD_PROCESOR = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    procesor_info()

def cancel_update_procesor(window, tree, b, d, f, nume_entry, nuclee_entry, threaduri_entry,
                                                              frecventa_entry, putere_entry, pret_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    nume_entry.delete(0, END)
    nuclee_entry.delete(0, END)
    threaduri_entry.delete(0, END)
    frecventa_entry.delete(0, END)
    putere_entry.delete(0, END)
    pret_entry.delete(0, END)

    procesor_info()

def select_record_procesor(event, parent):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        # show a message
   #print(record)

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("nuclee").insert(0, record[2])
    parent.children.get("threaduri").insert(0, record[3])
    parent.children.get("frecventa").insert(0, record[4])
    parent.children.get("putere").insert(0, record[5])
    parent.children.get("pret").insert(0, record[6])


def update_record_procesor(my_tree, nume, nuclee, threaduri, frecventa, putere, pret, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
                                            nume.get(), nuclee.get(), threaduri.get(), frecventa.get(),
                                            putere.get(), pret.get()))
    #print(frecventa.get())
    try:
        backend.cur.execute("""UPDATE Procesor SET
                        NUME = :nume,
                        NUCLEE = :nuclee,
                        THREADURI = :threaduri,
                        FRECVENTA = :frecventa,
                        PUTERE = :putere,
                        PRET = :pret
    
                        WHERE COD_PROCESOR = :id""",
                            {
                                'nume': nume.get(),
                                'nuclee': int(nuclee.get()),
                                'threaduri': int(threaduri.get()),
                                'frecventa': float(frecventa.get()),
                                'putere': float(putere.get()),
                                'pret': float(pret.get()),
                                'id': id.get()
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

def insert_into_produse(window, tree, b, d, f, s, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    backend.insert_into_table(table, list)
    produse_info()

def update_produse(my_tree, tip_produs_entry, clicked_comenzi, clicked_procesor, clicked_placa_video, clicked_memorie_ram,  id_entry, window, b, d, f, s):
    update_record_produse(my_tree, tip_produs_entry,
                          clicked_comenzi, clicked_procesor, clicked_placa_video, clicked_memorie_ram, id_entry)
    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    produse_info()

def produse_info():
    global my_tree
    all_tabels.forget()
    Produse.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#34312D",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Produse)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down,
                           selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[7][0])
    print(columns)
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0],
                          columns[5][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COD_PRODUS", anchor=W, width=100, stretch=NO)
    my_tree.column("TIP_PRODUS", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("COMENZI_COD_COMANDA", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("PROCESOR_COD_PROCESOR", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("PLACA_VIDEO_COD_PLACA_VIDEO", anchor=CENTER, width=225, stretch=NO)
    my_tree.column("MEMORIE_RAM_COD_RAM", anchor=CENTER, width=175, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COD_PRODUS", text="COD_PRODUS", anchor=W)
    my_tree.heading("TIP_PRODUS", text="TIP_PRODUS", anchor=CENTER)
    my_tree.heading("COMENZI_COD_COMANDA", text="COMENZI_COD_COMANDA", anchor=CENTER)
    my_tree.heading("PROCESOR_COD_PROCESOR", text="PROCESOR_COD_PROCESOR", anchor=CENTER)
    my_tree.heading("PLACA_VIDEO_COD_PLACA_VIDEO", text="PLACA_VIDEO_COD_PLACA_VIDEO", anchor=CENTER)
    my_tree.heading("MEMORIE_RAM_COD_RAM", text="MEMORIE_RAM_COD_RAM", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[7][0])
    # print(data)

    my_tree.tag_configure('oddrow', background="#A47551")
    my_tree.tag_configure('evenrow', background="#d9c5b2")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Produse, text="Introduceti datele:", background="#34312D", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    tip_produs = Label(data_frame, text="Tip_produs: ", background="#34312D", foreground="#E4D4C8")
    tip_produs.grid(row=0, column=0, padx=10, pady=10)
    tip_produs_entry = Entry(data_frame, background="#34312D", foreground="#E4D4C8", name="tip_produs")
    tip_produs_entry.grid(row=0, column=1, padx=65, pady=10)

    select_frame = LabelFrame(Produse, text="Alegeti datele:", background="#34312D", foreground="#E4D4C8")
    select_frame.pack(pady=0, padx=0, fill='x')

    tabela_comenzi = backend.select_from_table(backend.Table_names[3][0])
    tabela_procesor = backend.select_from_table(backend.Table_names[6][0])
    tabela_placa_video = backend.select_from_table(backend.Table_names[5][0])
    tabela_memorie_ram = backend.select_from_table(backend.Table_names[4][0])

    clicked_comenzi = StringVar(Produse)
    clicked_comenzi.set(tabela_comenzi[0])
    alege_comenzi = Label(select_frame, text="Alegeti comanda", background="#34312D", foreground="#E4D4C8")
    alege_comenzi.grid(row=0, column=0)
    drop_comenzi = OptionMenu(select_frame, clicked_comenzi, *tabela_comenzi)
    drop_comenzi.configure(background="#34312D", foreground="#E4D4C8", activebackground="#34312D",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_comenzi.grid(row=0, column=1, padx=0, pady=1)

    clicked_procesor = StringVar(Produse)
    clicked_procesor.set(tabela_procesor[0])
    alege_procesor = Label(select_frame, text="Alegeti procesor", background="#34312D", foreground="#E4D4C8")
    alege_procesor.grid(row=0, column=2)
    drop_comenzi = OptionMenu(select_frame, clicked_procesor, *tabela_procesor)
    drop_comenzi.configure(background="#34312D", foreground="#E4D4C8", activebackground="#34312D",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_comenzi.grid(row=0, column=3, padx=0, pady=1)

    clicked_placa_video = StringVar(Produse)
    clicked_placa_video.set(tabela_placa_video[0])
    alege_placa_video = Label(select_frame, text="Alegeti placa video", background="#34312D", foreground="#E4D4C8")
    alege_placa_video.grid(row=1, column=0)
    drop_placa_video = OptionMenu(select_frame, clicked_placa_video, *tabela_placa_video)
    drop_placa_video.configure(background="#34312D", foreground="#E4D4C8", activebackground="#34312D",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_placa_video.grid(row=1, column=1, padx=0, pady=1)

    clicked_memorie_ram = StringVar(Produse)
    clicked_memorie_ram.set(tabela_memorie_ram[0])
    alege_memorie_ram = Label(select_frame, text="Alegeti memorie ram", background="#34312D", foreground="#E4D4C8")
    alege_memorie_ram.grid(row=1, column=2)
    drop_memorie_ram = OptionMenu(select_frame, clicked_memorie_ram, *tabela_memorie_ram)
    drop_memorie_ram.configure(background="#34312D", foreground="#E4D4C8", activebackground="#34312D",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_memorie_ram.grid(row=1, column=3, padx=0, pady=1)

    button_frame = LabelFrame(Produse, text="Comenzi", background="#34312D", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=1)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#34312D", fg="#D9C5B2",
                        command=lambda: insert_into_produse(Produse, my_tree, data_frame, button_frame, tree_frame,
                                                            select_frame,
                                                            backend.Table_names[7][0],
                                                            [None,
                                                             tip_produs_entry.get(),
                                                             int(clicked_comenzi.get().replace(',', '     ')[1:4]),
                                                             int(clicked_procesor.get().replace(',', '     ')[1:4]),
                                                             int(clicked_placa_video.get().replace(',', '     ')[1:4]),
                                                             int(clicked_memorie_ram.get().replace(',', '     ')[1:4])])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    back = Button(Produse, text="Inapoi", font=("Arial", 12), bg="#34312D", fg="#D9C5B2",
                  command=lambda: back_selection(Produse))
    back.place(x=840, y=515)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_produse(my_tree, tip_produs_entry,
                                                          clicked_comenzi, clicked_procesor, clicked_memorie_ram, clicked_memorie_ram, id_entry,
                                                          Comenzi, data_frame, button_frame, tree_frame, select_frame)
                           , bg="#34312D", fg="#D9C5B2")
    update_button.grid(row=0, column=2, padx=10, pady=10)
    # foreign_key = [tabela_clienti[0][0], tabela_angajati[0][0], tabela_adrese[0][0]]
    # print(foreign_key)
    my_tree.bind('<<TreeviewSelect>>',
                 lambda e: select_record_produse(e, data_frame, clicked_comenzi, clicked_procesor, clicked_placa_video, clicked_memorie_ram,
                                                 tabela_comenzi, tabela_procesor, tabela_placa_video, tabela_memorie_ram))

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_produse(Produse, my_tree, data_frame, button_frame, tree_frame,
                                                            select_frame,
                                                                 tip_produs_entry),
                           background="#34312D", foreground="#D9C5B2")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_produse(my_tree, id_entry, Produse, data_frame,
                                                                 button_frame, tree_frame, select_frame)
                           , bg="#34312D", fg="#D9C5B2")
    remove_button.grid(row=0, column=4, padx=10, pady=10)


def remove_record_produse(my_tree, id, window, b, d, f, s):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.cur.execute("""DELETE FROM Produse
                WHERE COD_PRODUS = :id""",
                            {
                                'id': id.get(),
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    procesor_info()

def cancel_update_produse(window, tree, b, d, f, s, tip_produs_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    tip_produs_entry.delete(0, END)

    produse_info()

def select_record_produse(event, parent, comenzi, procesor, placa_video, memorie_ram, tc, tp, tpv, tmr):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']
        # print(record[3], record[4], record[5])
        # show a message
    # print(record)

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("tip_produs").insert(0, record[1])
    comenzi.set(tc[record[2]-1])
    procesor.set(tp[record[3]])
    placa_video.set(tpv[record[4]])
    memorie_ram.set(tmr[record[5]])

def update_record_produse(my_tree, tip_produs_entry,
                          clicked_comenzi, clicked_procesor, clicked_placa_video, clicked_memorie_ram, id_entry):
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    try:
        backend.cur.execute("""UPDATE Produse SET
            TIP_PRODUS = :tip_produs,
            COMENZI_COD_COMANDA = :ccc,
            PROCESOR_COD_PROCESOR = :pcp,
            PLACA_VIDEO_COD_PLACA_VIDEO = :pvcpv,
            MEMORIE_RAM_COD_RAM = :mrcmr
    
            WHERE COD_PRODUS = :id""",
                            {
                                'tip_produs': tip_produs_entry.get(),
                                'ccc': int(clicked_comenzi.get().replace(',', '     ')[1:4]),
                                'pcp': int(clicked_procesor.get().replace(',', '     ')[1:4]),
                                'pvcpv': int(clicked_placa_video.get().replace(',', '     ')[1:4]),
                                'mrcmr': int(clicked_memorie_ram.get().replace(',', '     ')[1:4]),
                                'id': id_entry.get()
                            })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

def add_savepoint(savePointName, popup):
    global savepoints
    #print("SAVEPOINT " + str(savePointName))
    try:
        backend.cur.execute("SAVEPOINT " + str(savePointName))
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    if (savepoints.qsize() == 5):
        savepoints.get()
        savepoints.put(savePointName)
    else:
        savepoints.put(savePointName)

    popup.destroy()


def savepoint():
    savePoint_name = StringVar()
    popup = tkinter.Toplevel()
    popup.title('Savepoints')
    #popup.geometry('100x100')
    popup.configure(background="#34312D")
    label = tkinter.Label(popup, text="Savepoint", font=("Arial", 10), background="#34312D",
                          foreground="#D9C5B2")
    label.pack()
    Entry(popup, textvariable=savePoint_name, width=30).pack()

    ok_button = Button(popup, text="OK", command=lambda: add_savepoint(savePoint_name.get(), popup), background="#34312D", foreground="#D9C5B2")
    ok_button.pack()
    '''
    try:
        backend.cur.execute("SAVEPOINT Random")
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)
        '''

def rollback_to_savepoint(name, popup):
    global savepoints

    try:
        backend.cur.execute("ROLLBACK TO " + str(name))
        savepoints.queue.remove(name)
    except Exception as err:
        message = "Error while using rollback: " + str(err)
        messagebox.showerror(title='Error', message=message)

    popup.destroy()
    rollback()

def commit():
    try:
        backend.cur.execute("COMMIT")
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

def rollback():
    global savepoints
    popup = tkinter.Toplevel()
    popup.title('Rollbacks')
    #popup.geometry('400x200')
    popup.configure(background="#34312D")
    label = tkinter.Label(popup, text="Rollback la savepoint", font=("Arial", 10), background="#34312D", foreground="#D9C5B2")
    label.pack()
    #for element in savepoints.queue:
    #    print(element)
    for i in range(savepoints.qsize()):
        button = tkinter.Button(popup, text=savepoints.queue[i], command=lambda: rollback_to_savepoint(savepoints.queue[i], popup), background="#34312D", foreground="#D9C5B2")
        button.pack()

if __name__ == "__main__":
    #backend.Table_names = backend.connection('Nume', 'pass', 'localhost', '1521', 'xe')
    backend.Table_names = backend.connection('bd017', 'bd017', 'bd-dc.cs.tuiasi.ro', '1539', 'orcl')
    root = Tk()
    root.title("DB Manager")
    root.geometry("900x600")
    root.resizable(False, False)
    root.configure(background="#14110F")
    root.iconbitmap("database.ico")
    my_menu = Menu(root)
    root.config(menu=my_menu)

    my_menu.add_command(label="Commit", command=commit)
    my_menu.add_command(label="Rollback", command=rollback)
    my_menu.add_command(label="Savepoint", command=savepoint)

    menuinfo()

    root.mainloop()
    backend.close_connection()
