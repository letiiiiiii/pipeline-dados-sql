import pandas as pd
import sqlite3
from pathlib import Path

# definindo caminhos
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "vendas.csv"
DB_PATH = BASE_DIR / "pipeline.db"

def extract(path=DATA_PATH):
    df = pd.read_csv(path)
    return df

def transform(df):
    df['data'] = pd.to_datetime(df['data'])
    df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce').fillna(0).astype(int)
    df['preco_unitario'] = pd.to_numeric(df['preco_unitario'], errors='coerce').fillna(0.0)
    df['total'] = df['quantidade'] * df['preco_unitario']
    return df

def load(df, db_path=DB_PATH, table_name="vendas"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def main():
    print("Iniciando pipeline ETL...")
    df = extract()
    df_clean = transform(df)
    load(df_clean)
    print("Pipeline finalizado! Registros carregados:", len(df_clean))

if __name__ == "__main__":
    main()
