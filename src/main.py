from extract import read_transactions_csv
from transform import transform_transaction_list
from load import create_database, insert_transactions

def main()->None:

    transactions = read_transactions_csv("./data/raw/transactions.csv")

    transformed_list = transform_transaction_list(transactions)


    create_database(
        "data/output/transactions.db",
        "sql/create_tables.sql"
    )

    insert_transactions("data/output/transactions.db", transformed_list)
    print("Transactions inserted successfully.")

    print(f"Read {len(transactions)} transactions from CSV.")
    print(f"Inserted {len(transformed_list)} transactions into SQLite.")

if __name__ == "__main__":
    main()