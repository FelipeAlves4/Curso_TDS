CREATE TABLE IF NOT EXISTS funcionarios (
    id_funcionario INT PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    salario DECIMAL(10, 2),
    data_contratacao DATE
);

INSERT INTO funcionarios (id_funcionario, nome, cargo, salario, data_contratacao) VALUES 
(1, 'Ana Silva', 'Desenvolvedora', 5000.00, '2023-01-10'),
 (2, 'João Santos', 'Analista de Sistemas', 4500.00, '2022-06-15'),
 (3, 'Maria Oliveira', 'Gerente de Projetos', 7000.00, '2021-03-22');


UPDATE funcionarios
SET cargo = 'Desenvolvedora Sênior', salario = 6000.00
WHERE id_funcionario = 1;


DELETE FROM funcionarios 
WHERE id_funcionario = 2;