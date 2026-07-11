from src.extract import read_transactions_csv

def test_read_transactions_csv(tmp_path):
    csv_file= tmp_path/"transactions.csv"
    csv_file.write_text(
        "transaction_id,account_id,merchant_id,transaction_time,amount,currency,status,channel\n"
        "1001,101,201,2024-02-01 09:15:00,85.40,NZD,approved,card\n",
        encoding="utf-8",
    )

    csv_file_list = read_transactions_csv(csv_file)

    assert len(csv_file_list) ==1

    assert csv_file_list[0]["transaction_id"] == "1001"
    assert csv_file_list[0]["amount"] == "85.40"
    assert csv_file_list[0]["currency"] == "NZD"