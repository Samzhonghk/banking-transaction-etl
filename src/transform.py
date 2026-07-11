from extract import read_transactions_csv

def transform_transaction(transaction: dict[str,str])-> dict[str, str|int|float]:
        

    return{
        "transaction_id": int(transaction["transaction_id"]),
        "account_id": int(transaction["account_id"]),
        "merchant_id": int(transaction["merchant_id"]),
        "transaction_time": transaction["transaction_time"],
        "amount": float(transaction["amount"]),
        "currency": transaction["currency"],
        "status": transaction["status"],
        "channel": transaction["channel"],

    }

def transform_transaction_list(transaction_list: list[dict[str,str]])->list[dict[str,int|float|str]]:
    transformed_list = []
    for t in transaction_list:
        single_transformed_item = transform_transaction(t)
        transformed_list.append(single_transformed_item)
    return transformed_list