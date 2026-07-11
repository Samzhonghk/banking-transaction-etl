import csv

def read_transactions_csv(file_path: str)-> list[dict[str, str]]:
    transactions = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions