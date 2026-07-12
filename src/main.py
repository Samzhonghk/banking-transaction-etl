import argparse
import logging
from extract import read_transactions_csv
from transform import transform_transaction_list
from load import create_database, insert_transactions
from validate import validate_transactions


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

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

    try:


        transactions = read_transactions_csv(args.input)

        transformed_list = transform_transaction_list(transactions)

        valid_transactions = validate_transactions(transformed_list)


        create_database(
            args.database,
            args.schema,
        )

        insert_transactions(args.database, valid_transactions)
        print("Transactions inserted successfully.")

    except FileNotFoundError as error:
        logging.error("File not found: %s", error.filename)
        raise SystemExit(1) from error

    # print(f"Read {len(transactions)} transactions from CSV.")
    # print(f"Inserted {len(transformed_list)} transactions into SQLite.")
    logging.info("Read %s transactions from CSV.", len(transactions))
    logging.info("Transformed %s transactions.", len(transformed_list))
    logging.info("Validated %s transactions.", len(valid_transactions))
    logging.info("Inserted %s transactions into SQLite", len(transformed_list))

if __name__ == "__main__":
    main()