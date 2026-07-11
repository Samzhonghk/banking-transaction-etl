from src.transform import transform_transaction_list, transform_transaction

def test_transform_transaction_converted_types():
    raw_transaction = {
        "transaction_id": "1001",
        "account_id": "101",
        "merchant_id": "201",
        "transaction_time": "2024-02-01 09:15:00",
        "amount": "85.40",
        "currency": "NZD",
        "status": "approved",
        "channel": "card"
    }

    transformed_transaction = transform_transaction(raw_transaction)
    assert transformed_transaction["transaction_id"] == 1001
    assert transformed_transaction["account_id"] == 101
    assert transformed_transaction["merchant_id"] == 201
    assert transformed_transaction["transaction_time"] == '2024-02-01 09:15:00'
    assert transformed_transaction["amount"] == 85.40

def test_transform_transaction_list_convert_multi_transactions():
    raw_transactions = [
        {
            "transaction_id": "1001",
            "account_id": "101",
            "merchant_id": "201",
            "transaction_time": "2024-02-01 09:15:00",
            "amount": "85.40",
            "currency": "NZD",
            "status": "approved",
            "channel": "card",
        },
        {
            "transaction_id": "1002",
            "account_id": "101",
            "merchant_id": "202",
            "transaction_time": "2024-02-01 12:30:00",
            "amount": "60.00",
            "currency": "NZD",
            "status": "approved",
            "channel": "card",
        },
    ]

    transformed_list = transform_transaction_list(raw_transactions)
    assert len(transformed_list) == 2
    transformed_list[0]["status"] == "approved"
    transformed_list[1]["amount"] == 60.00