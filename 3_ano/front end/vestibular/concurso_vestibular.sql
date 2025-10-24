CREATE TABLE Cidades_Prova (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_cidade VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL
);

CREATE TABLE Cursos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_curso VARCHAR(100) NOT NULL
);

CREATE TABLE Horarios_Prova (
    id INT PRIMARY KEY AUTO_INCREMENT,
    descricao_horario VARCHAR(50) NOT NULL
);

CREATE TABLE Candidatos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_completo VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    rg VARCHAR(20) NOT NULL,
    orgao_emissor VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    mao_predominante ENUM('destro', 'canhoto') NOT NULL,
    necessidade_especial BOOLEAN NOT NULL DEFAULT FALSE,
    descricao_necessidade TEXT,
    cidade_prova_id INT,
    curso_id INT,
    horario_prova_id INT,
    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cidade_prova_id) REFERENCES Cidades_Prova(id),
    FOREIGN KEY (curso_id) REFERENCES Cursos(id),
    FOREIGN KEY (horario_prova_id) REFERENCES Horarios_Prova(id)
);

CREATE TABLE Enderecos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    candidato_id INT NOT NULL UNIQUE,
    cep VARCHAR(9),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    FOREIGN KEY (candidato_id) REFERENCES Candidatos(id) ON DELETE CASCADE
);

CREATE TABLE Telefones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    candidato_id INT NOT NULL,
    tipo ENUM('celular', 'residencial', 'comercial') NOT NULL,
    numero VARCHAR(20) NOT NULL,
    FOREIGN KEY (candidato_id) REFERENCES Candidatos(id) ON DELETE CASCADE
);