import sqlite3

from src.extract import read_transactions_csv
from src.transform import transform_transaction_list
from src.load import create_database, insert_transactions

def test_full_pipeline(tmp_path):
    db_file = tmp_path/"transactions.db"
    csv_file = tmp_path/"transactions.csv"

    csv_file.write_text(
        "transaction_id,account_id,merchant_id,transaction_time,amount,currency,status,channel\n"
        "1001,101,201,2024-02-01 09:15:00,85.40,NZD,approved,card\n",
        encoding="utf-8",
    )

    raw_transform_file = read_transactions_csv(csv_file)
    transformed_list = transform_transaction_list(raw_transform_file)

    create_database(db_file, "sql/create_tables.sql")
    insert_transactions(db_file, transformed_list)

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM transactions")
    result = cursor.fetchone()
    connection.close()

    assert result[0] == 1