import csv

def write_rejected_transactions(
        file_path: str, 
        transactions: list[dict[str, str|int|float]],
)-> None:
    if not transactions:
        return
    
    fieldnames = list(transactions[0].keys())
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)