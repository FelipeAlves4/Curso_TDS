CREATE TABLE Candidatos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_completo VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    rg VARCHAR(20) NOT NULL,
    orgao_emissor VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    mao_predominante ENUM('destro', 'canhoto') NOT NULL,
    cidade_prova_id INT,
    curso_id INT,
    horario_prova_id INT,
    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cidade_prova_id) REFERENCES Cidades_Prova(id),
    FOREIGN KEY (curso_id) REFERENCES Cursos(id),
    FOREIGN KEY (horario_prova_id) REFERENCES Horarios_Prova(id)
);

CREATE TABLE Telefones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    candidato_id INT NOT NULL,
    tipo ENUM('celular', 'residencial', 'comercial') NOT NULL,
    numero VARCHAR(20) NOT NULL,
    FOREIGN KEY (candidato_id) REFERENCES Candidatos(id) ON DELETE CASCADE
);


CREATE TABLE Candidatos_Necessidades (
    candidato_id INT NOT NULL,
    necessidade_id INT NOT NULL,
    PRIMARY KEY (candidato_id, necessidade_id),
    FOREIGN KEY (candidato_id) REFERENCES Candidatos(id) ON DELETE CASCADE,
    FOREIGN KEY (necessidade_id) REFERENCES Necessidades_Especiais_Opcoes(id) ON DELETE CASCADE
);


CREATE TABLE Horarios_Prova (
    id INT PRIMARY KEY AUTO_INCREMENT,
    descricao_horario VARCHAR(50) NOT NULL
);

CREATE TABLE Estados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    uf CHAR(2) NOT NULL UNIQUE
);

CREATE TABLE Cidades (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    estado_id INT NOT NULL,
    FOREIGN KEY (estado_id) REFERENCES Estados(id)
);

CREATE TABLE Cidades_Prova (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cidade_id INT NOT NULL,
    FOREIGN KEY (cidade_id) REFERENCES Cidades(id)
);
