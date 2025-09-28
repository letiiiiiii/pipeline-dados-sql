CREATE TABLE IF NOT EXISTS vendas (
    id_venda INTEGER PRIMARY KEY,
    data DATE,
    produto TEXT,
    quantidade INTEGER,
    preco_unitario REAL,
    total REAL
);
