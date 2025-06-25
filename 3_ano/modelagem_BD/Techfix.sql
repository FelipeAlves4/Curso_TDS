
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT  PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    cidade VARCHAR(50),
    data_nascimento DATE
);


CREATE TABLE  IF NOT EXISTS produtos (
    id_produto INT  PRIMARY KEY AUTOINCREMENT,
    nome_produto VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    fabricante VARCHAR(50),
    estoque INT
);

CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER  PRIMARY KEY AUTOINCREMENT,
    id_cliente INT,
    data_pedido DATE,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

ALTER TABLE clientes 
ADD COLUMN telefone_secundario VARCHAR(15);


ALTER TABLE produtos 
DROP COLUMN fabricante;


ALTER TABLE pedidos 
MODIFY COLUMN data_pedido DATETIME;


ALTER TABLE produtos 
ADD COLUMN peso DECIMAL(5,2), 
ADD COLUMN dimensao VARCHAR(50);


ALTER TABLE clientes 
MODIFY COLUMN nome VARCHAR(100) NOT NULL;