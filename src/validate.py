VALID_STATUS = {
    "approved",
    "failed",
    "flagged"
}

def validate_transaction(transaction:dict[str,str|int|float])->bool:
    if transaction["amount"]<0:
        return False
    
    if transaction["status"] not in VALID_STATUS:
        return False
    
    return True

def validate_transactions(
        transactions: list[dict[str, str|int|float]]
)-> list[dict[str, int|str|float]]:
    valid_transactions = []
    for t in transactions:
        if validate_transaction(t):
            valid_transactions.append(t)
    return valid_transactions