import json

VALID_STATUS = {
    "approved",
    "failed",
    "flagged"
}

def validate_transaction(
        transaction:dict[str,str|int|float],
        rules: dict[str, list[str]|int|float]
        )->bool:
    # if transaction["amount"]<0:
    #     return False
    
    # if transaction["status"] not in VALID_STATUS:
    #     return False
    if transaction["amount"]<rules["min_amount"]:
        return False
    
    if transaction["status"] not in rules["allowed_statuses"]:
        return False
    
    return True

def validate_transactions(
        transactions: list[dict[str, str|int|float]],
        rules: dict[str, list[str]|int|float]
)-> list[dict[str, int|str|float]]:
    valid_transactions = []
    for t in transactions:
        if validate_transaction(t, rules):
            valid_transactions.append(t)
    return valid_transactions

def split_valid_invalid_transactions(
        ts: list[dict[str, str|int|float]],
        rules: dict[str, list[str]|int|float]
)->tuple[
    list[dict[str, str|int|float]],
    list[dict[str, str|int|float]]
]:
    valid_transations = []
    invalid_transactions = []

    for t in ts:
        if validate_transaction(t, rules):
            valid_transations.append(t)
        else:
            invalid_transactions.append(t)

    return valid_transations, invalid_transactions


def load_validation_rules(file_path: str)->dict[str, str|int|float]:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)