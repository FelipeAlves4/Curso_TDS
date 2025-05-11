START TRANSACTION;

-- Inserir nova venda
INSERT INTO Vendas (id_venda, id_cliente, id_produto, data_venda)
VALUES (6, 3, 3, CURDATE());

-- Atualizar estoque
UPDATE Produtos
SET estoque = estoque - 1
WHERE id_produto = 3;

-- Verificar se há estoque suficiente
SELECT estoque INTO @estoque_atual FROM Produtos WHERE id_produto = 3 FOR UPDATE;

IF @estoque_atual >= 0 THEN
    COMMIT;
    SELECT 'Transação confirmada com sucesso!' AS Resultado;
ELSE
    ROLLBACK;
    SELECT 'Erro: Estoque insuficiente. Transação revertida.' AS Resultado;
END IF;

START TRANSACTION;

-- Inserir venda
INSERT INTO Vendas (id_venda, id_cliente, id_produto, data_venda)
VALUES (7, 2, 1, CURDATE());

-- Simular erro (estoque negativo)
UPDATE Produtos
SET estoque = estoque - 100  -- Valor que deixará estoque negativo
WHERE id_produto = 1;

-- Verificação condicional
SELECT estoque INTO @estoque_resultante FROM Produtos WHERE id_produto = 1;

IF @estoque_resultante >= 0 THEN
    COMMIT;
ELSE
    ROLLBACK;
    SELECT 'ERRO: Estoque ficaria negativo. Transação revertida.' AS Mensagem;
END IF;

-- Sessão 1
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;

-- Consulta que bloqueará outros acessos
SELECT * FROM Produtos WHERE id_produto = 2 FOR UPDATE;

-- Manter esta transação aberta para testar concorrência
-- (Não fazer COMMIT ainda)

-- Sessão 2 (testar em outra conexão)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;

-- Esta consulta ficará aguardando a Sessão 1 liberar o lock
SELECT * FROM Produtos WHERE id_produto = 2 FOR UPDATE;
-- Timeout ocorrerá se a Sessão 1 não liberar


-- Relatório diário que não precisa de consistência absoluta
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;

-- Relatório que pode mostrar dados já confirmados
SELECT * FROM Vendas WHERE data_venda = CURDATE();

COMMIT;