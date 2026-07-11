import sqlite3

from src.load import create_database, insert_transactions

def test_create_database_and_insert_transactions(tmp_path):
    # tmp_path = "./tmp_path/"
    db_path = tmp_path / "test.transactions.db"
    schema_path = "sql/create_tables.sql"

    transactions = [
        {
            "transaction_id": 1001,
            "account_id": 101,
            "merchant_id": 201,
            "transaction_time": "2024-02-01 09:15:00",
            "amount": 85.40,
            "currency": "NZD",
            "status": "approved",
            "channel": "card",
        }
    ]

    create_database(str(db_path), schema_path)
    insert_transactions(str(db_path), transactions)

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM transactions")
    count = cursor.fetchone()[0]

    connection.close()

    assert count == 1