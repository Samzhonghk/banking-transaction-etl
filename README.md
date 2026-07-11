# Banking Transaction ETL

A small Python ETL project that reads banking transaction data from CSV, transforms data types, and loads the cleaned records into a SQLite database.

## ETL Flow

```text
CSV file
  -> extract.py
  -> transform.py
  -> load.py
  -> SQLite database


然后继续加：

```md
## What This Project Demonstrates

- Reading CSV files with Python
- Transforming raw string data into typed records
- Loading data into SQLite
- Separating ETL logic into extract, transform, and load modules
- Writing unit tests and full pipeline tests with pytest
- Running code quality checks with Ruff

## Project Structure

```text
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



然后可以再加一个小节：

```md
## Command Line Options

| Option | Description | Default |
| --- | --- | --- |
| `--input` | Path to the input transactions CSV file | `data/raw/transactions.csv` |
| `--database` | Path to the output SQLite database | `data/output/transactions.db` |
| `--schema` | Path to the SQL schema file | `sql/create_tables.sql` |