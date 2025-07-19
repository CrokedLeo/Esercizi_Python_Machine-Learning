
-- 1 tabelle con vincoli
create table if not exists Sale 
(CodiceSala int primary key,
Nome varchar(100) not null,
Citta varchar(100),
Posti int check(Posti > 10));

create table if not exists Film
(CodiceFilm int primary key,
Titolo varbinary(100) not null,
AnnoProduzione year check (AnnoProduzione > 1900),
Genere varchar(50),
Regista varchar(100));

create table if not exists Proiezioni
(codProiezione int primary key auto_increment,
CodFilm int not null,
CodSala int not null,
Incasso float,
DataProiezione date,
foreign key (CodFilm) references Film(CodiceFilm),
foreign key (CodSala) references Sale(CodiceSala));

insert into Sale(CodiceSala, Nome, Citta, posti) values
(1, 'Sala Grande', 'Roma', 100),
(2, 'Sala VIP', 'Napoli', 50);

insert into Film(CodiceFilm, Titolo, AnnoProduzione, Genere, Regista) values
(1, 'Inception', 2010, 'Thriller', 'Christopher Nolan'),
(2, 'Parasite', 2019, NULL, 'Bong Joon-ho');

insert into Proiezioni (CodFilm, CodSala, Incasso, DataProduzione) values
(1, 1, 2500.50, '2024-06-01'),
(2, 2, 1800.00, '2024-06-02'),
(1, 2, NULL, '2024-06-03');

