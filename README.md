# Banking Transaction ETL

A small Python ETL project that reads banking transaction data from CSV, transforms data types, and loads the cleaned records into a SQLite database.

## ETL Flow

CSV file
  -> extract.py
  -> transform.py
  -> validate.py
  -> load.py
  -> SQLite database


## What This Project Demonstrates

- Reading CSV files with Python
- Transforming raw string data into typed records
- Loading data into SQLite
- Separating ETL logic into extract, transform, and load modules
- Writing unit tests and full pipeline tests with pytest
- Running code quality checks with Ruff

- Validating transaction data before loading
- Rejecting invalid records such as negative transaction amounts
- Logging ETL progress and validation results

## Project Structure

banking-transaction-etl/
  data/
    raw/
    output/
  sql/
    create_tables.sql
  src/
    extract.py
    transform.py
    load.py
    main.py
  tests/
    test_extract.py
    test_transform.py
    test_load.py
    test_pipeline.py


## How To Run
python .\src\main.py

## Run with custom paths:
python .\src\main.py --input data/raw/transactions.csv --database data/output/transactions.db --schema sql/create_tables.sql

## Run Test
python -m pytest

## Code Quality
python -m ruff check .



## Command Line Options

| Option | Description | Default |
| --- | --- | --- |
| `--input` | Path to the input transactions CSV file | `data/raw/transactions.csv` |
| `--database` | Path to the output SQLite database | `data/output/transactions.db` |
| `--schema` | Path to the SQL schema file | `sql/create_tables.sql` |


## Data Validation

The pipeline validates transformed transactions before loading them into SQLite.

Current validation rules:

- `amount` must not be negative
- `status` must be one of `approved`, `failed`, or `flagged`

Invalid records are excluded from loading, and the number of rejected records is logged during the ETL run.


## Run Logging / Observability

Each ETL run writes a record into the `etl_run_logs` table.

The log captures:

- input CSV file path
- output SQLite database path
- number of records read
- number of records transformed
- number of valid records
- number of rejected records
- number of inserted records
- run timestamp

Example query:

```sql
SELECT *
FROM etl_run_logs
ORDER BY run_id DESC;


## Configurable Validation Rules

Validation rules are stored in:

config/validation_rules.json

Example:
{
  "allowed_statuses": ["approved", "failed", "flagged"],
  "min_amount": 0
}