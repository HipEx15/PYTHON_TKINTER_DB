--inserare date in tabela clienti

INSERT INTO clienti (cod_client, nume, prenume, email) VALUES (NULL, 'Popescu', 'Ionescu', 'popescuion@gmail.com');
INSERT INTO clienti (cod_client, nume, prenume, email) VALUES (NULL, 'Mihai', 'Cosmin', 'mihaicosmin@gmail.com');
INSERT INTO clienti (cod_client, nume, prenume, email) VALUES (NULL, 'Doceanu', 'Daniel Bogdan', 'danielbogdan@yahoo.com');
INSERT INTO clienti (cod_client, nume, prenume, email) VALUES (NULL, 'Paul', 'Andrei Dragos', 'paulandrei@yahoo.com');
INSERT INTO clienti (cod_client, nume, prenume, email) VALUES (NULL, 'Ailenei', 'Ioana', 'ioanaailenei@gmail.com');

select * from clienti;

--inserare date in tabela adrese

INSERT INTO adrese (cod_adresa, strada, oras, judet, tara, cod_postal, numar_telefon) VALUES (NULL, 'Strada Academiei nr. 7', 'Bucuresti', 'Bucuresti', 'Romania', '010011', '0745 824 552');
INSERT INTO adrese (cod_adresa, strada, oras, judet, tara, cod_postal, numar_telefon) VALUES (NULL, 'Strada Amurgului nr. 35', 'Constanta', 'Constanta', 'Romania', '900005', '0785 423 195');
INSERT INTO adrese (cod_adresa, strada, oras, judet, tara, cod_postal, numar_telefon) VALUES (NULL, 'Strada Vuia Traian', 'Brasov', 'Brasov', 'Romania', '500008', '0768 793 226');
INSERT INTO adrese (cod_adresa, strada, oras, judet, tara, cod_postal, numar_telefon) VALUES (NULL, 'Strada Donici Alexandru', 'Sibiu', 'Sibiu', 'Romania', '550010', '0769 224 458');
INSERT INTO adrese (cod_adresa, strada, oras, judet, tara, cod_postal, numar_telefon) VALUES (NULL, 'Strada Lalescu Traian bl. 11, a3', 'Craiova', 'Dolj', 'Romania', '200012', '0753 124 835');

select * from adrese;

--inserare date in tabela de angajati

INSERT INTO angajati(cod_angajat, nume, prenume, data_nastere, numar_telefon, email, data_angajare, salariu, comision) VALUES (NULL, 'Basarab', 'Marcel', to_date('12.07.1990','DD.MM.YYYY'), '0753 282 842', NULL, to_date('05.11.2016','DD.MM.YYYY'), '3700', '5');
INSERT INTO angajati(cod_angajat, nume, prenume, data_nastere, numar_telefon, email, data_angajare, salariu, comision) VALUES (NULL, 'Horiceanu', 'Ioana Elena', to_date('20.04.1995','DD.MM.YYYY'), '0752 749 911', NULL, to_date('02.08.2020','DD.MM.YYYY'), '2400', '3');
INSERT INTO angajati(cod_angajat, nume, prenume, data_nastere, numar_telefon, email, data_angajare, salariu, comision) VALUES (NULL, 'Roman', 'Bogdan', to_date('18.02.1987','DD.MM.YYYY'), '0724 222 536', 'romanbogdan@gmail.com', to_date('03.05.2010','DD.MM.YYYY'), '5000', '7');
INSERT INTO angajati(cod_angajat, nume, prenume, data_nastere, numar_telefon, email, data_angajare, salariu, comision) VALUES (NULL, 'Romica', 'Ionut', to_date('15.03.1990','DD.MM.YYYY'), '0755 232 413', NULL, to_date('03.05.2014','DD.MM.YYYY'), '4300', '5');
INSERT INTO angajati(cod_angajat, nume, prenume, data_nastere, numar_telefon, email, data_angajare, salariu, comision) VALUES (NULL, 'Malin', 'Dragos', to_date('01.04.1996','DD.MM.YYYY'), '0787 531 328', 'malindragos@gmail.com', to_date('03.05.2019','DD.MM.YYYY'), '2800', '3');

select * from angajati;

--inserare date in tabela procesor

insert into procesor values (0, 'NULL', 1, 1, 1, 1, 1);
insert into procesor values (null, 'AMD Ryzen 9 7900X', 12, 24, 4.70, 170, 2593);
insert into procesor values (null, 'Intel Core i3 10105F', 4, 8, 3.70, 65, 415);
insert into procesor values (null, 'AMD Ryzen 5 5600', 6, 12, 3.50, 65, 727);
insert into procesor values (null, 'Intel Core i7 11700F', 8, 16, 2.50, 65, 1380);
insert into procesor values (null, 'AMD Ryzen 7 7700X', 8, 16, 4.50, 105, 1896);

select * from procesor;

--inserare date in tabela placa video

insert into Placa_video values (0, 'NULL', 'NULL', 0, 0, 0, 0);
insert into Placa_video values (null, 'Gainward GeForce RTX 3060', 'GDDR6', 12, 1777, 170, 2030);
insert into Placa_video values (null, 'MSI Radeon RX 6750 XT', 'GDDR6', 12, 2620, 250, 2350);
insert into Placa_video values (null, 'Palit GeForce RTX 4080', 'GDDR6X', 16, 2505, 320, 7300);
insert into Placa_video values (null, 'Gainward GeForce RTX 3050', 'GDDR6', 8, 1777, 130, 1752);
insert into Placa_video values (null, 'GIGABYTE Radeon RX 6400', 'GDDR6', 4, 2321 , 53, 810);

select * from Placa_video;

--inserare date in tabela memorie ram

insert into Memorie_ram values (0, 'NULL', 'NULL', 0, 0, 'NULL', 'Nu', 0);
insert into Memorie_ram values (null, 'Corsair Vengeance LPX Black', 'DDR4', 16, 3200, 'PC4 25600', 'Da', 292);
insert into Memorie_ram values (null, 'Kingston FURY Beast', 'DDR5', 32, 5200, 'PC5 41600', 'Da', 872);
insert into Memorie_ram values (null, 'Kingston ValueRAM', 'DDR4', 8, 2666, 'PC4 21300', 'Nu', 143);
insert into Memorie_ram values (null, 'Kingston FURY Beast', 'DDR4', 64, 3200, 'PC4 25600', 'Da', 1049);
insert into Memorie_ram values (null, 'Zeppelin', 'DDR3', 4, 1333, 'PC3 10600', 'Nu', 63);

select * from Memorie_ram;

--inserare date in tabela comenzi

INSERT INTO comenzi VALUES (NULL, to_date('22.11.2022','DD.MM.YYYY'), 'cash', (select cod_client from clienti where cod_client='1'), (select cod_angajat from angajati where cod_angajat='1'), (select cod_adresa from adrese where cod_adresa='1'));
INSERT INTO comenzi VALUES (NULL, to_date('21.11.2022','DD.MM.YYYY'), 'card', (select cod_client from clienti where cod_client='2'), (select cod_angajat from angajati where cod_angajat='3'), (select cod_adresa from adrese where cod_adresa='2'));
INSERT INTO comenzi VALUES (NULL, to_date('16.11.2022','DD.MM.YYYY'), 'card', (select cod_client from clienti where cod_client='3'), (select cod_angajat from angajati where cod_angajat='2'), (select cod_adresa from adrese where cod_adresa='3'));
INSERT INTO comenzi VALUES (NULL, to_date('10.11.2022','DD.MM.YYYY'), 'cash', (select cod_client from clienti where cod_client='4'), (select cod_angajat from angajati where cod_angajat='5'), (select cod_adresa from adrese where cod_adresa='4'));
INSERT INTO comenzi VALUES (NULL, to_date('17.11.2022','DD.MM.YYYY'), 'card', (select cod_client from clienti where cod_client='5'), (select cod_angajat from angajati where cod_angajat='4'), (select cod_adresa from adrese where cod_adresa='5'));

select * from comenzi;

--inserare date in tabela produse
INSERT INTO produse VALUES (NULL, 'Memorie ram', (select cod_comanda from comenzi where cod_comanda='1'), 
                            0, 0, (select cod_ram from memorie_ram where cod_ram='1'));
INSERT INTO produse VALUES (NULL, 'Procesor', (select cod_comanda from comenzi where cod_comanda='2'), 
                            (select cod_procesor from procesor where cod_procesor='3'), 0, 0); 
INSERT INTO produse VALUES (NULL, 'Placa video', (select cod_comanda from comenzi where cod_comanda='3'), 
                            0, (select cod_placa_video from placa_video where cod_placa_video='5'), 0);
INSERT INTO produse VALUES (NULL, 'Placa video', (select cod_comanda from comenzi where cod_comanda='4'), 
                            0, (select cod_placa_video from placa_video where cod_placa_video='3'), 0); 
INSERT INTO produse VALUES (NULL, 'Procesor', (select cod_comanda from comenzi where cod_comanda='5'), 
                            (select cod_procesor from procesor where cod_procesor='1'), 0, 0);

select * from produse;