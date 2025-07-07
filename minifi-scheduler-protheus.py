#!/usr/bin/env python3

import pyodbc
import csv
from datetime import datetime

# Configurações de conexão - ajuste para seu banco Protheus
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SEU_SERVIDOR;"
    "DATABASE=SEU_BANCO;"
    "UID=SEU_USUARIO;"
    "PWD=SUA_SENHA;"
)

query = """
SELECT * FROM sua_tabela
WHERE data >= '2024-01-01'
"""

csv_path = "/var/minifi/output/protheus_data.csv"

def main():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(query)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Cabeçalhos
        writer.writerow([desc[0] for desc in cursor.description])
        # Dados
        for row in cursor:
            writer.writerow(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
