CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  preco DECIMAL(10,2)
);

CREATE TABLE vendas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente INT,
  id_produto INT,
  data_venda DATE,
  quantidade INT,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id),
  FOREIGN KEY (id_produto) REFERENCES produtos(id)
);

CREATE VIEW relatorio_vendas AS
SELECT 
  c.nome AS cliente, 
  p.nome AS produto, 
  v.data_venda, 
  v.quantidade
FROM vendas v
JOIN clientes c ON v.id_cliente = c.id
JOIN produtos p ON v.id_produto = p.id;

SELECT * FROM relatorio_vendas;


SELECT * 
FROM relatorio_vendas
WHERE quantidade > 10;


CREATE TABLE relatorio_vendas_materializada AS
SELECT 
  c.nome AS cliente, 
  p.nome AS produto, 
  v.data_venda, 
  v.quantidade,
  p.preco
FROM vendas v
JOIN clientes c ON v.id_cliente = c.id
JOIN produtos p ON v.id_produto = p.id
WHERE p.preco > 100;


SELECT * FROM relatorio_vendas_materializada;

DROP TABLE relatorio_vendas_materializada;

CREATE TABLE relatorio_vendas_materializada AS
SELECT 
  c.nome AS cliente, 
  p.nome AS produto, 
  v.data_venda, 
  v.quantidade,
  p.preco
FROM vendas v
JOIN clientes c ON v.id_cliente = c.id
JOIN produtos p ON v.id_produto = p.id
WHERE p.preco > 100;
