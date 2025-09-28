# pipeline-dados-sql

## Descrição
Este projeto implementa uma **pipeline de dados** que lê um arquivo CSV de vendas, transforma os dados utilizando Python/Pandas e carrega em um banco de dados PostgreSQL. É um exemplo de ETL (Extract, Transform, Load) para manipulação de dados de vendas fictícias.

## Estrutura do Projeto

pipeline-dados-sql/
│
├── README.md
├── data/
│ └── vendas.csv
├── src/
│ └── pipeline.py
├── scripts/
│ └── create_tables.sql
└── requirements.txt

- `data/vendas.csv` → dataset bruto (pode ser fictício de vendas).  
- `src/pipeline.py` → script que realiza ETL: lê o CSV, transforma os dados com pandas e carrega em um banco.  
- `scripts/create_tables.sql` → script SQL para criar a tabela no banco.  
- `requirements.txt` → bibliotecas necessárias para rodar o projeto.  
- `README.md` → explicação do projeto.

## Tecnologias
- Python 3.x  
- Pandas  
- SQL (PostgreSQL)  

## Pré-requisitos
- Python instalado  
- PostgreSQL rodando localmente ou em servidor remoto  
- Bibliotecas do `requirements.txt` instaladas  

## Como Rodar

1. Clonar o repositório:

```bash
git clone <https://github.com/letiiiiiii/pipeline-dados-sql>
cd pipeline-dados-sql


