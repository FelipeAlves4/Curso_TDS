CREATE TABLE IF NOT EXISTS autores (
    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_autor VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS livros (
    id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(150) NOT NULL,
    id_autor INTEGER,
    id_categoria INTEGER,
    preco DECIMAL(10, 2),
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

ALTER TABLE livros
ADD data_publicacao DATE;


CREATE TABLE IF NOT EXISTS editoras (
    id_editora INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_editora VARCHAR(100) NOT NULL
);


ALTER TABLE livros
ADD id_editora INTEGER;

ALTER TABLE livros
ADD FOREIGN KEY (id_editora) REFERENCES editoras(id_editora);


ALTER TABLE livros
ADD quantidade_estoque INTEGER NOT NULL DEFAULT 0;

ALTER TABLE livros
ADD num_paginas INTEGER;

ALTER TABLE livros
ADD CONSTRAINT check_estoque_positivo CHECK (quantidade_estoque >= 0);