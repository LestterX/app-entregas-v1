CREATE TABLE IF NOT EXISTS ordens(
    id INTEGER PRIMARY KEY,
    cliente TEXT NOT NULL,
    endereco TEXT NOT NULL,
    telefone TEXT NOT NULL,
    valor TEXT NOT NULL,
    forma_pagamento TEXT NOT NULL,
    pago TEXT NOT NULL,
    entregue TEXT NOT NULL,
    descricao TEXT NOT NULL,
    coletado TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS sites(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    link TEXT NOT NULL
);