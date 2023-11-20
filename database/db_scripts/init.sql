CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE animal (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    especie VARCHAR(50),
    dono_id INTEGER REFERENCES cliente(id)
);

CREATE TABLE consulta (
    id SERIAL PRIMARY KEY,
    data DATE,
    animal_id INTEGER REFERENCES animal(id),
    descricao TEXT
);

INSERT INTO cliente (nome, telefone) VALUES
    ('Cliente1', '111-1111'),
    ('Cliente2', '222-2222'),
    ('Cliente3', '333-3333'),
    ('Cliente4', '444-4444'),
    ('Cliente5', '555-5555'),
    ('Cliente6', '666-6666');

INSERT INTO animal (nome, especie, dono_id) VALUES
    ('Cachorro1', 'Cachorro', 1),
    ('Gato1', 'Gato', 2),
    ('Pássaro1', 'Pássaro', 3),
    ('Cachorro2', 'Cachorro', 4),
    ('Gato2', 'Gato', 5),
    ('Pássaro2', 'Pássaro', 6);

INSERT INTO consulta (data, animal_id, descricao) VALUES
    ('2023-01-01', 1, 'Banho e Tosa'),
    ('2023-02-01', 2, 'Tratamento de alergia'),
    ('2023-03-01', 3, 'Verificação anual'),
    ('2023-04-01', 4, 'Consulta de vacinação'),
    ('2023-05-01', 5, 'Tratamento de ferida'),
    ('2023-06-01', 6, 'Check-up de saúde');

