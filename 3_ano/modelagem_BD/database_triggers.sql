-- Criando as tabelas necessárias
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    data_cadastro DATE
);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    data_pedido DATE,
    status VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE auditoria_pedidos (
    id_auditoria INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT,
    data_atualizacao DATETIME,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

-- Trigger 1: Exclusão automática de pedidos relacionados quando um cliente é excluído
DELIMITER //
CREATE TRIGGER after_cliente_delete
AFTER DELETE ON clientes
FOR EACH ROW
BEGIN
    DELETE FROM pedidos WHERE id_cliente = OLD.id_cliente;
END //
DELIMITER ;

-- Trigger 2: Registro de auditoria para atualizações de pedidos
DELIMITER //
CREATE TRIGGER after_pedido_update
AFTER UPDATE ON pedidos
FOR EACH ROW
BEGIN
    INSERT INTO auditoria_pedidos (id_pedido, data_atualizacao)
    VALUES (NEW.id_pedido, NOW());
END //
DELIMITER ;

-- Trigger 3: Prevenir exclusão de pedidos com status 'Enviado'
DELIMITER //
CREATE TRIGGER before_pedido_delete
BEFORE DELETE ON pedidos
FOR EACH ROW
BEGIN
    IF OLD.status = 'Enviado' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Não é possível excluir pedido com status Enviado';
    END IF;
END //
DELIMITER ;

-- Trigger Criativo: Rastreamento automático de status VIP para clientes frequentes
-- Nova tabela para rastrear status VIP
CREATE TABLE clientes_vip (
    id_cliente INT PRIMARY KEY,
    total_pedidos INT DEFAULT 0,
    vip_status BOOLEAN DEFAULT FALSE,
    ultima_atualizacao DATETIME,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Trigger para atualizar status VIP com base na frequência de pedidos
DELIMITER //
CREATE TRIGGER after_pedido_insert
AFTER INSERT ON pedidos
FOR EACH ROW
BEGIN
    DECLARE pedido_count INT;
    
    -- Atualiza ou insere na tabela clientes_vip
    INSERT INTO clientes_vip (id_cliente, total_pedidos, ultima_atualizacao)
    VALUES (NEW.id_cliente, 1, NOW())
    ON DUPLICATE KEY UPDATE 
        total_pedidos = total_pedidos + 1,
        ultima_atualizacao = NOW();
    
    -- Verifica o total de pedidos e atualiza o status VIP
    SELECT total_pedidos INTO pedido_count 
    FROM clientes_vip 
    WHERE id_cliente = NEW.id_cliente;
    
    IF pedido_count >= 5 THEN
        UPDATE clientes_vip 
        SET vip_status = TRUE 
        WHERE id_cliente = NEW.id_cliente;
    END IF;
END //
DELIMITER ;

-- Exemplo de uso para testes
-- Inserir dados de exemplo
INSERT INTO clientes (id_cliente, nome, email, data_cadastro)
VALUES (1, 'João Silva', 'joao@email.com', '2025-01-01');

INSERT INTO pedidos (id_pedido, id_cliente, data_pedido, status)
VALUES (1, 1, '2025-01-02', 'Pendente');

-- Atualizar status do pedido
UPDATE pedidos SET status = 'Enviado' WHERE id_pedido = 1;

-- Tentar excluir pedido (deve falhar se status for 'Enviado')
-- DELETE FROM pedidos WHERE id_pedido = 1;

-- Excluir cliente (deve excluir pedidos em cascata)
-- DELETE FROM clientes WHERE id_cliente = 1;

-- Inserir múltiplos pedidos para testar status VIP
INSERT INTO pedidos (id_pedido, id_cliente, data_pedido, status)
VALUES 
    (2, 1, '2025-02-01', 'Pendente'),
    (3, 1, '2025-03-01', 'Pendente'),
    (4, 1, '2025-04-01', 'Pendente'),
    (5, 1, '2025-05-01', 'Pendente'),
    (6, 1, '2025-06-01', 'Pendente');