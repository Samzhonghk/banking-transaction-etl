CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    merchant_id INTEGER NOT NULL,
    transaction_time TEXT NOT NULL,
    amount REAL NOT NULL,
    currency TEXT NOT NULL,
    status TEXT NOT NULL,
    channel TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS etl_run_logs (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_time TEXT NOT NULL,
    input_file TEXT NOT NULL,
    database_file TEXT NOT NULL,
    total_read INTEGER NOT NULL,
    total_transformed INTEGER NOT NULL,
    total_valid INTEGER NOT NULL,
    total_rejected INTEGER NOT NULL,
    total_inserted INTEGER NOT NULL
);