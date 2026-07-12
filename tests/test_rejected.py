from src.rejected import write_rejected_transactions

def test_write_rejected_transactions(tmp_path):
    output_file = tmp_path / "rejected_transaction.csv"

    ts = [
        {
            "transaction_id": 1002,
            "account_id": 101,
            "merchant_id": 202,
            "transaction_time": "2024-02-01 12:30:00",
            "amount": -60.00,
            "currency": "NZD",
            "status": "approved",
            "channel": "card",
        }
    ]

    write_rejected_transactions(str(output_file), ts)
    content = output_file.read_text("utf-8")

    assert "transaction_id,account_id,merchant_id" in content
    assert "1002,101,202" in content
    assert "-60.0" in content