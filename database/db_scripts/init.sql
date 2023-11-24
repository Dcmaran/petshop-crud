CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE animal (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    especie VARCHAR(50),
    dono_id INTEGER REFERENCES cliente(id) ON DELETE CASCADE
);

CREATE TABLE consulta (
    id SERIAL PRIMARY KEY,
    data DATE,
    animal_id INTEGER REFERENCES animal(id) ON DELETE CASCADE,
    descricao TEXT
);

INSERT INTO cliente (nome, telefone) VALUES
    ('João Silva', '111-1111'),
    ('Maria Santos', '222-2222'),
    ('Carlos Oliveira', '333-3333'),
    ('Ana Souza', '444-4444'),
    ('Fernando Costa', '555-5555'),
    ('Isabel Lima', '666-6666');

INSERT INTO animal (nome, especie, dono_id) VALUES
    ('Cachorro1', 'Cachorro', 1),
    ('Gato1', 'Gato', 2),
    ('Pássaro1', 'Pássaro', 3),
    ('Cachorro2', 'Cachorro', 4),
    ('Gato2', 'Gato', 2),
    ('Pássaro2', 'Pássaro', 6);

INSERT INTO consulta (data, animal_id, descricao) VALUES
    ('2023-01-01', 1, 'Banho e Tosa'),
    ('2023-02-01', 2, 'Adestramento'),
    ('2023-03-01', 3, 'Hospedagem'),
    ('2023-04-01', 4, 'Banho'),
    ('2023-05-01', 5, 'Daycare'),
    ('2023-06-01', 6, 'Ensaio Fotográfico');

