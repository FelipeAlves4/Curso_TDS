CREATE TABLE  if not EXISTS Produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    preco DECIMAL(10, 2)
);

INSERT INTO Produtos (id_produto, nome_produto, preco)
VALUES
    (1, 'Televisão', 1500.00),
    (2, 'Geladeira', 2000.00),
    (3, 'Micro-ondas', 500.00);

CREATE TABLE if not EXISTS Vendas_Clientes (
    id_venda INT,
    id_cliente INT,
    FOREIGN KEY (id_venda) REFERENCES Vendas(id_venda),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

INSERT INTO Vendas_Clientes (id_venda, id_cliente)
SELECT v.id_venda, c.id_cliente
FROM Vendas v
JOIN Clientes c ON v.id_cliente = c.id_cliente
WHERE YEAR(v.data_venda) = 2024;

-- Criação das novas tabelas
CREATE TABLE if not EXISTS Fornecedores (
    id_fornecedor INT PRIMARY KEY,
    nome_fornecedor VARCHAR(100) NOT NULL,
    cidade VARCHAR(50)
);

CREATE TABLE if not EXISTS Categorias (
    id_categoria INT PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL
);

CREATE TABLE if not EXISTS Produtos_Categorias (
    id_produto INT,
    id_categoria INT,
    PRIMARY KEY (id_produto, id_categoria),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto),
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

-- Inserção das categorias
INSERT INTO Categorias (id_categoria, nome_categoria)
VALUES
    (1, 'Eletrodomésticos'),
    (2, 'Eletroportáteis');

-- Solução do desafio: Inserção com JOIN
INSERT INTO Produtos_Categorias (id_produto, id_categoria)
SELECT p.id_produto, 
       CASE 
           WHEN p.nome_produto IN ('Televisão', 'Geladeira') THEN 1
           WHEN p.nome_produto = 'Micro-ondas' THEN 2
       END AS id_categoria
FROM Produtos p
WHERE p.nome_produto IN ('Televisão', 'Geladeira', 'Micro-ondas');

-- Alternativa mais explícita
INSERT INTO Produtos_Categorias (id_produto, id_categoria)
SELECT p.id_produto, c.id_categoria
FROM Produtos p
CROSS JOIN Categorias c
WHERE (p.nome_produto IN ('Televisão', 'Geladeira') AND c.nome_categoria = 'Eletrodomésticos')
   OR (p.nome_produto = 'Micro-ondas' AND c.nome_categoria = 'Eletroportáteis');