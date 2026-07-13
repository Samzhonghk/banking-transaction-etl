import argparse
import logging
from extract import read_transactions_csv
from transform import transform_transaction_list
from load import create_database, insert_transactions, insert_etl_run_log
# from validate import validate_transactions
from rejected import write_rejected_transactions
from validate import split_valid_invalid_transactions, load_validation_rules


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

    parse.add_argument(
        "--rejected_output",
        default="data/output/rejected_transactions.csv",
        help="Path to the rejected transactions csv file."
    )

    parse.add_argument(
        "--rules",
        default="config/validations_rules.json",
        help="Path to the validation rules file"
    )

    return parse.parse_args()

def main()->None:

    args = parse_args()

    try:


        transactions = read_transactions_csv(args.input)
        rules = load_validation_rules(args.rules)

        transformed_list = transform_transaction_list(transactions)

        valid_transactions, invalid_transactions = split_valid_invalid_transactions(transformed_list,rules)

        invalid_count = len(invalid_transactions)



        create_database(
            args.database,
            args.schema,
        )

        insert_transactions(args.database, valid_transactions)
        insert_etl_run_log(
            args.database,
            args.input,
            args.database,
            len(transactions),
            len(transformed_list),
            len(valid_transactions),
            len(invalid_transactions),
            len(valid_transactions)

        )
        write_rejected_transactions(args.rejected_output, invalid_transactions)
        print("Transactions inserted successfully.")

    except FileNotFoundError as error:
        logging.error("File not found: %s", error.filename)
        raise SystemExit(1) from error

    # print(f"Read {len(transactions)} transactions from CSV.")
    # print(f"Inserted {len(transformed_list)} transactions into SQLite.")
    logging.info("Read %s transactions from CSV.", len(transactions))
    logging.info("Transformed %s transactions.", len(transformed_list))
    logging.info("Validated %s transactions.", len(valid_transactions))
    logging.info("Rejected %s invalid transactions", invalid_count)
    logging.info("wrote rejected transactions to %s.", args.rejected_output)
    logging.info("Inserted %s transactions into SQLite", len(transformed_list))


if __name__ == "__main__":
    main()