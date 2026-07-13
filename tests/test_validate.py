
from src.validate import validate_transaction, validate_transactions, split_valid_invalid_transactions, load_validation_rules

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

    rules = {
        "allowed_statuses": ["approved", "flagged"],
        "min_amount": 0
    }

    assert validate_transaction(transaction, rules) is True

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

    rules = {
        "allowed_statuses": ["approved", "flagged"],
        "min_amount": 0
    }

    assert validate_transaction(transaction, rules) is False

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

    rules = {
        "allowed_statuses": ["approved", "flagged"],
        "min_amount": 0
    }

    valid_ts = validate_transactions(transactions,rules)
    assert len(valid_ts) == 1
    assert valid_ts[0]["transaction_id"] == 1001

def test_split_valid_invalid_transactions():
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
        },
        {
            "transaction_id": 1002,
            "account_id": 101,
            "merchant_id": 202,
            "transaction_time": "2024-02-01 12:30:00",
            "amount": -60.00,
            "currency": "NZD",
            "status": "approved",
            "channel": "card",
        },
    ]

    rules = {
        "allowed_statuses": ["approved", "flagged"],
        "min_amount": 0
    }

    valid_ts, invalid_ts = split_valid_invalid_transactions(transactions, rules)

    assert valid_ts[0]["transaction_id"] == 1001
    assert invalid_ts[0]["transaction_id"] == 1002
    assert len(valid_ts) == 1
    assert len(invalid_ts) == 1

def test_load_validation_rules(tmp_path):
    rules_file = tmp_path/"validation_rules.json"
    rules_file.write_text(
        """
        {
            "allowed_statuses": ["approved", "failed"],
            "min_amount": 0
        }
        """,
        encoding="utf-8",
    )

    rules = load_validation_rules(str(rules_file))
    assert rules["allowed_statuses"] == ["approved", "failed"]
    assert rules["min_amount"] == 0