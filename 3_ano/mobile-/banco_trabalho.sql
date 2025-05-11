CREATE TABLE IF NOT EXISTS Categoria(
    id integer PRIMARY KEY AUTOINCREMENT,
    nome text not null
);

CREATE TABLE IF NOT EXISTS Tarefas(
    id integer PRIMARY KEY AUTOINCREMENT,
    titulo text not null,
    descricao text,
    status integer not null, 
  	id_categoria integer,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
);

INSERT INTO Categoria(nome) VALUES
('Trabalho'),
('Pessoal'),
('Estudos'),
('Saúde'),
('Lazer'),
('Finanças'),
('Projetos'),
('Familia'),
('Viagem'),
('Codar');


INSERT INTO Tarefas(titulo, descricao, status, id_categoria) VALUES 
('Lavar Louça', NULL, 0, 8),
('Estudar SQL', 'Criar tabelas e inserir dados', 0, 3), 
('Calculadora', 'Criar uma calculadora em Python', 1, 10), 
('Code Experience', 'Fazer o curso Code Experience', 0, 2),
('Arrumar o quarto', NULL, 0, 8),
('Estudar Mobile', 'Revisar conceitos de SQLite e Flutter', 0, 3),
('Projeto de Site', 'Desenvolver um site com HTML e CSS', 1, 2),
('Treinar Python', 'Praticar exercícios de listas e dicionários', 0, 3),
('Fazer compras', 'Comprar materiais para o projeto', 0, 8),
('Terminar série', 'Assistir episódios finais', 1, 5);


SELECT COUNT(*) As Contagem_de_Categoria
From Categoria;

select * from Categoria;

SELECT * FROM Tarefas
WHERE status = 1;

Select * from Tarefas
WHERE id_categoria = 1;

INSERT INTO Tarefas(titulo, descricao, status, id_categoria) VALUES
('Enviar relatório', 'Finalizar e enviar relatório mensal', 0, 1), -- Trabalho
('Organizar armário', 'Separar roupas para doação', 0, 2), -- Pessoal
('Revisar SQL', 'Praticar comandos SELECT e INSERT', 0, 3), -- Estudos
('Consulta médica', 'Ir ao clínico geral para check-up', 0, 4), -- Saúde
('Maratona de filmes', 'Assistir trilogia favorita', 0, 5), -- Lazer
('Pagar boletos', 'Luz, água e internet', 0, 6), -- Finanças
('Criar novo app', 'Desenvolver um aplicativo simples', 0, 7), -- Projetos
('Almoço em família', 'Organizar almoço de domingo', 0, 8), -- Família
('Reservar hotel', 'Reservar hospedagem para a viagem', 0, 9), -- Viagem
('Estudar algoritmos', 'Praticar algoritmos no LeetCode', 0, 10); -- Codar


SELECT * FROM Tarefas
WHERE id_categoria = 9;

SELECT * FROM Tarefas
WHERE id_categoria = 8;

SELECT * FROM Tarefas 
order by titulo ASC;

SELECT descricao FROM Tarefas
WHERE status = 1;

SELECT titulo from Tarefas
WHERE id_categoria < 5;

SELECT * FROM Tarefas
WHERE descricao LIKE '%app%';

SELECT titulo FROM Tarefas
WHERE LENGTH(titulo) > 20;

SELECT Tarefas.titulo, Tarefas.descricao, Tarefas.status, Categoria.nome AS nome_categoria
FROM Tarefas
JOIN Categoria ON Tarefas.id_categoria = Categoria.id;

SELECT Categoria.nome
FROM Categoria
LEFT JOIN Tarefas ON Categoria.id = Tarefas.id_categoria
WHERE Tarefas.id_categoria IS NULL;

SELECT Tarefas.titulo, Tarefas.descricao, Categoria.nome AS nome_categoria
FROM Tarefas
JOIN Categoria ON Tarefas.id_categoria = Categoria.id
WHERE Tarefas.status = 1;

SELECT Tarefas.titulo, Categoria.nome AS nome_categoria
FROM Tarefas
JOIN Categoria ON Tarefas.id_categoria = Categoria.id
WHERE Tarefas.status = 0;

SELECT Tarefas.titulo, Tarefas.descricao
FROM Tarefas
JOIN Categoria ON Tarefas.id_categoria = Categoria.id
WHERE Categoria.nome = 'Projetos';

SELECT COUNT(*) As Contagem_de_tarefas
From Tarefas;

SELECT status, COUNT(*) AS quantidade
FROM Tarefas
GROUP BY status;

SELECT Categoria.nome AS categoria, COUNT(Tarefas.id) AS quantidade_tarefas
FROM Categoria
LEFT JOIN Tarefas ON Categoria.id = Tarefas.id_categoria
GROUP BY Categoria.nome
ORDER BY quantidade_tarefas DESC;

SELECT Categoria.nome AS categoria, COUNT(Tarefas.id) AS quantidade_tarefas
FROM Categoria
LEFT JOIN Tarefas ON Categoria.id = Tarefas.id_categoria
GROUP BY Categoria.nome
ORDER BY quantidade_tarefas DESC
LIMIT 1;

SELECT Categoria.nome AS categoria, COUNT(Tarefas.id) AS quantidade_tarefas
FROM Categoria
LEFT JOIN Tarefas ON Categoria.id = Tarefas.id_categoria
GROUP BY Categoria.nome
ORDER BY quantidade_tarefas ASC
LIMIT 1;

UPDATE Tarefas
SET status = 1
WHERE id_categoria = (SELECT id FROM Categoria WHERE nome = 'Familia');
SELECT * from Tarefas
WHERE id_categoria = 8;

DELETE FROM Tarefas
WHERE id_categoria = (SELECT id FROM Categoria WHERE nome = 'Viagem');
SELECT * from Tarefas 
WHERE id_categoria = 9;

INSERT into Tarefas(titulo, descricao, status, id_categoria) VALUES
('Fazer trabalho de mobile', NULL, 0, 3);
SELECT * FROM Tarefas
WHERE id_categoria = 3;

UPDATE Tarefas
SET descricao = 'Criar tabelas e inserir dados e prática com JOINs'
WHERE titulo = 'Estudar SQL';
SELECT * from Tarefas
WHERE titulo = 'Estudar SQL';

UPDATE Tarefas
SET id_categoria = (SELECT id FROM Categoria WHERE nome = 'Familia')
WHERE id_categoria = (SELECT id FROM Categoria WHERE nome = 'Pessoal');

