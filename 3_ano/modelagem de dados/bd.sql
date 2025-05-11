CREATE DATABASE minha_loja;  -- Cria um banco de dados

USE minha_loja;  -- Seleciona o banco de dados (no MySQL)

CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    idade INT
); -- Cria uma tabela

INSERT INTO clientes (nome, email, idade) 
VALUES ('Felipe Alves', 'felipe@email.com', 25);

SELECT * FROM clientes; -- Retorna todos os clientes

SELECT nome, email FROM clientes WHERE idade > 18; -- Filtra por idade

CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    produto VARCHAR(100),
    valor DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);
