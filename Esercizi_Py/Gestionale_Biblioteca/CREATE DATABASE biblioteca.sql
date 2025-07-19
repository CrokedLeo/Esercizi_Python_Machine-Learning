CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE utenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ruolo ENUM('amministratore', 'utente') DEFAULT 'utente'
);

CREATE TABLE libri (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titolo VARCHAR(200) NOT NULL,
    autore VARCHAR(200) NOT NULL,
    disponibile BOOLEAN DEFAULT TRUE,
    utente_id INT DEFAULT NULL,
    FOREIGN KEY (utente_id) REFERENCES utenti(id)
);
