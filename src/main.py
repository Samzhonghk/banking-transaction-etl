from extract import read_transactions_csv
from transform import transform_transaction_list
from load import create_database, insert_transactions

transactions = read_transactions_csv("./data/raw/transactions.csv")

print(transactions)
print(len(transactions))

transformed_list = []
transformed_list = transform_transaction_list(transactions)


create_database(
    "data/output/transactions.db",
    "sql/create_tables.sql"
)

insert_transactions("data/output/transactions.db", transformed_list)
print("Transactions inserted successfully.")
# for t in transactions:
#     transformed_transaction = transform_transaction(t)
#     transformed_list.append(transformed_transaction)

# print("------------------------------")
# print(transformed_list)
# print("CURRENCY-------"+transformed_list[0]["currency"])
# print(type(transformed_list[0]["amount"]))

# print("data created successfully")