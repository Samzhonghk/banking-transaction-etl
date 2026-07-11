import sqlite3

def create_database(db_path: str, schema_path: str)-> None:
    with open(schema_path, "r", encoding="utf-8") as file:
        schema_sql = file.read()
    connection = sqlite3.connect(db_path)

    try:
        connection.executescript(schema_sql)
        connection.commit()
    finally:
        connection.close()

def insert_transactions(
        db_path: str,
        transactions: list[dict[str,str|int|float]]
    
)-> None:
    connection = sqlite3.connect(db_path)

    try:
        cursor = connection.cursor()
        for transaction in transactions:
            cursor.execute(
                """
                INSERT OR REPLACE INTO transactions (
                    transaction_id,
                    account_id,
                    merchant_id,
                    transaction_time,
                    amount,
                    currency,
                    status,
                    channel
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    transaction["transaction_id"],
                    transaction["account_id"],
                    transaction["merchant_id"],
                    transaction["transaction_time"],
                    transaction["amount"],
                    transaction["currency"],
                    transaction["status"],
                    transaction["channel"]
                )
            )
        connection.commit()

    finally:
        connection.close()