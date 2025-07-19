create database if not exists cinema;
use cinema;


create table Sale
(CodSala int primary key,
NomeSala varchar(100) not null);

create table Film
(ID int primary key auto_increment,
Titolo varchar(100) not null unique,
AnnoProduzione int not null check(AnnoProduzione >= 1900 ),
Regista varchar(100) not null,
Genere varchar(50));

alter table Film
add column Durata int default 90;

alter table Film
add column CodSala int;

alter table Film
add constraint fk_cod_sala
foreign key(CodSala) references Sale(CodSala);

alter table Film
drop column Genere;

insert into Sale (CodSala, NomeSala)
values (1, 'sala vip'), (2, 'sala base');

-- dati esempio
INSERT INTO Film (Titolo, AnnoProduzione, Regista, Durata, CodSala)
VALUES
  ('Inception', 2010, 'Christopher Nolan', 148, 1),
  ('La Vita è Bella', 1997, 'Roberto Benigni', DEFAULT, 2),
  ('Parasite', 2019, 'Bong Joon-ho', 132, NULL);


