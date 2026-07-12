from src.validate import validate_transaction, validate_transactions

def test_validate_transaction_accepts_valid_transaction():
    transaction = {
        "transaction_id": 1001,
        "account_id": 101,
        "merchant_id": 201,
        "transaction_time": "2024-02-01 09:15:00",
        "amount": 85.40,
        "currency": "NZD",
        "status": "approved",
        "channel": "card",
    }

    assert validate_transaction(transaction) is True

def test_validate_transaction_rejects_valid_transaction()->bool:
    transaction = {
        "transaction_id": 1001,
        "account_id": 101,
        "merchant_id": 201,
        "transaction_time": "2024-02-01 09:15:00",
        "amount": -1,
        "currency": "NZD",
        "status": "approved",
        "channel": "card",
    }

    assert validate_transaction(transaction) is False

def test_validate_transactions_invalid_list():
    transactions=[
        {
        "transaction_id": 1001,
        "account_id": 101,
        "merchant_id": 201,
        "transaction_time": "2024-02-01 09:15:00",
        "amount": 85.40,
        "currency": "NZD",
        "status": "approved",
        "channel": "card",
        },
        {
        "transaction_id": 1001,
        "account_id": 101,
        "merchant_id": 201,
        "transaction_time": "2024-02-01 09:15:00",
        "amount": -1,
        "currency": "NZD",
        "status": "approved",
        "channel": "card",
        }
    ]

    valid_ts = validate_transactions(transactions)
    assert len(valid_ts) == 1
    assert valid_ts[0]["transaction_id"] == 1001