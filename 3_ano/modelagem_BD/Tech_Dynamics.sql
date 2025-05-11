CREATE TABLE IF not EXISTS Clientes (
  id_cliente INT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  data_ultima_compra DATE,
  status VARCHAR(50)
);

-- Inserir dados na tabela Clientes
INSERT INTO Clientes (id_cliente, nome, email, data_ultima_compra, status) VALUES
(1, 'Ana Souza', 'ana@email.com', '2021-02-15', 'ativo'),
(2, 'Carlos Lima', 'carlos@email.com', '2019-08-10', 'inativo'),
(3, 'João Pedro', 'joao@email.com', '2020-12-05', 'ativo'),
(4, 'Mariana Silva', 'mariana@email.com', '2018-11-22', 'inadimplente'),
(5, 'Paula Costa', 'paula@email.com', '2017-07-09', 'inadimplente');

CREATE TABLE Produtos (
  id_produto INT PRIMARY KEY,
  nome_produto VARCHAR(100),
  preco DECIMAL(10, 2),
  estoque INT,
  data_entrada DATE,
  status VARCHAR(50)
);

    -- Inserir dados na tabela Produtos
INSERT INTO Produtos (id_produto, nome_produto, preco, estoque, data_entrada, status) VALUES
(1, 'Notebook X1', 3500.00, 10, '2021-01-15', 'disponível'),
(2, 'Smartphone Z5', 1200.00, 0, '2019-05-20', 'fora de estoque'),
(3, 'Tablet A7', 900.00, 15, '2020-09-10', 'disponível'),
(4, 'Câmera D500', 2200.00, 0, '2018-03-25', 'fora de estoque');

CREATE TABLE Fornecedores (
  id_fornecedor INT PRIMARY KEY,
  nome_fornecedor VARCHAR(100)
);

-- Inserir dados na tabela Fornecedores
INSERT INTO Fornecedores (id_fornecedor, nome_fornecedor) VALUES
(1, 'TechCorp'),
(2, 'Fornecedor Desconhecido'),
(3, 'Eletronix Solutions');

CREATE TABLE Fornecedores_Produtos (
  id_fornecedor INT,
  id_produto INT,
  PRIMARY KEY (id_fornecedor, id_produto),
  FOREIGN KEY (id_fornecedor) REFERENCES Fornecedores(id_fornecedor),
  FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

-- Inserir dados na tabela Fornecedores_Produtos
INSERT INTO Fornecedores_Produtos (id_fornecedor, id_produto) VALUES
(1, 1),
(2, 2),
(2, 4),
(3, 3);

CREATE TABLE Vendas (
  id_venda INT PRIMARY KEY,
  id_cliente INT,
  id_produto INT,
  data_venda DATE,
  FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
  FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

-- Inserir dados na tabela Vendas
INSERT INTO Vendas (id_venda, id_cliente, id_produto, data_venda) VALUES
(1, 1, 1, '2021-03-10'),
(2, 3, 2, '2020-06-25'),
(3, 4, 3, '2019-04-17'),
(4, 5, 4, '2018-12-19');

-- Verificação prévia (Boa prática)
SELECT * FROM Clientes
WHERE status = 'inativo'
AND data_ultima_compra < DATE_SUB(CURRENT_DATE(), INTERVAL 3 YEAR);

-- Execução da exclusão
DELETE FROM Clientes
WHERE status = 'inativo'
AND data_ultima_compra < DATE_SUB(CURRENT_DATE(), INTERVAL 3 YEAR);

-- Verificação prévia
SELECT p.* FROM Produtos p
JOIN Fornecedores_Produtos fp ON p.id_produto = fp.id_produto
JOIN Fornecedores f ON fp.id_fornecedor = f.id_fornecedor
WHERE f.nome_fornecedor = 'Fornecedor Desconhecido';

-- Execução da exclusão
DELETE p FROM Produtos p
JOIN Fornecedores_Produtos fp ON p.id_produto = fp.id_produto
JOIN Fornecedores f ON fp.id_fornecedor = f.id_fornecedor
WHERE f.nome_fornecedor = 'Fornecedor Desconhecido';

-- Verificação prévia
SELECT v.* FROM Vendas v
JOIN Clientes c ON v.id_cliente = c.id_cliente
WHERE c.status = 'inadimplente';

-- Execução da exclusão
DELETE v FROM Vendas v
JOIN Clientes c ON v.id_cliente = c.id_cliente
WHERE c.status = 'inadimplente';

-- Modelo para todas as tarefas:
-- 1. Primeiro crie uma consulta SELECT que identifique os registros
-- 2. Verifique se são exatamente os registros que deseja excluir
-- 3. Substitua o SELECT por DELETE mantendo as mesmas condições

-- Exemplo para Tarefa 2:
-- Passo 1: Consulta de verificação
SELECT COUNT(*) AS registros_afetados 
FROM Produtos p
JOIN Fornecedores_Produtos fp ON p.id_produto = fp.id_produto
JOIN Fornecedores f ON fp.id_fornecedor = f.id_fornecedor
WHERE f.nome_fornecedor = 'Fornecedor Desconhecido';

