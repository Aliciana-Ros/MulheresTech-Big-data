-- Criando meu primeiro banco de dados
CREATE DATABASE senac_copacanaba;

-- criando minha primeira tabela/entidade
CREATE TABLE alunos (
  Matricula INTEGER PRIMARY KEY,
  nome_aluno TEXT NOT NULL,
  gênero TEXT NOT NULL
);
-- injeção de dados
INSERT INTO alunos VALUES (1, 'Mariana', 'F');
INSERT INTO alunos VALUES (2, 'Joanna', 'F');
-- consultando as injeções
SELECT * FROM alunos WHERE gender = 'F';

-- Criar tabela 'cursos'
CREATE TABLE cursos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    carga_horaria INT,
    preco DECIMAL(10, 2),
    data_inicio DATE
);

-- Criar tabela 'filiais'
CREATE TABLE filiais (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    telefone VARCHAR(20)
);
