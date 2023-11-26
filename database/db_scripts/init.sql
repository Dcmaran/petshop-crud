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
    ('João Silva', '1111-1111'),
    ('Maria Santos', '2222-2222'),
    ('Carlos Oliveira', '3333-3333'),
    ('Ana Souza', '4444-4444'),
    ('Fernando Costa', '5555-5555'),
    ('Isabel Lima', '6666-6666');

INSERT INTO animal (nome, especie, dono_id) VALUES
    ('Belinha', 'Cachorro', 1),
    ('Alfredo', 'Gato', 2),
    ('Amarelinho', 'Pássaro', 3),
    ('Dengo', 'Cachorro', 4),
    ('Mia', 'Gato', 2),
    ('Piu Piu', 'Pássaro', 6);

INSERT INTO consulta (data, animal_id, descricao) VALUES
    ('2023-01-01', 1, 'Banho e Tosa'),
    ('2023-02-01', 2, 'Adestramento'),
    ('2023-03-01', 3, 'Hospedagem'),
    ('2023-04-01', 4, 'Banho'),
    ('2023-05-01', 5, 'Daycare'),
    ('2023-06-01', 6, 'Ensaio Fotográfico');

