from extract import read_transactions_csv
from transform import transform_transaction_list
from load import create_database, insert_transactions
import argparse

def parse_args():
    parse = argparse.ArgumentParser(
        description="Run banking transaction ETL pipeline"
    )

    parse.add_argument(
        "--input",
        default="data/raw/transactions.csv",
        help="Path to the input transaction csv file"
    )

    parse.add_argument(
        "--database",
        default="data/output/transactions.db",
        help="Path to the output of SQLite database"

    )

    parse.add_argument(
        "--schema",
        default="sql/create_tables.sql",
        help="Path to the SQL schema file."
    )

    return parse.parse_args()

def main()->None:

    args = parse_args()


    transactions = read_transactions_csv(args.input)

    transformed_list = transform_transaction_list(transactions)


    create_database(
        args.database,
        args.schema,
    )

    insert_transactions(args.database, transformed_list)
    print("Transactions inserted successfully.")

    print(f"Read {len(transactions)} transactions from CSV.")
    print(f"Inserted {len(transformed_list)} transactions into SQLite.")

if __name__ == "__main__":
    main()