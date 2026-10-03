# 001
import pandas as pd

customer_master = pd.read_csv('customer_master.csv', encoding='utf-8')
# print(customer_master[0:5])
item_master = pd.read_csv('item_master.csv', encoding='utf-8')
transaction_1 = pd.read_csv('transaction_1.csv', encoding='utf-8')
transaction_2 = pd.read_csv('transaction_2.csv', encoding='utf-8')
transaction_detail_1 = pd.read_csv('transaction_detail_1.csv', encoding='utf-8')
transaction_detail_2 = pd.read_csv('transaction_detail_2.csv', encoding='utf-8')


# print(item_master.head(1))
# print(transaction_1.head(1))
# print(transaction_2.iloc[[0]])
# print(transaction_detail_1.iloc[[0]])
# print(transaction_detail_2.iloc[[0]])


# 002
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
# print(transaction.head(3))
# print(f'1 is {len(transaction_1)}')
# print(f'2 is {len(transaction_2)}')
# print(f'concat is {len(transaction)}')

transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
# print(transaction_detail.head(3))
# print(f'1 is {len(transaction_detail_1)}')
# print(f'2 is {len(transaction_detail_2)}')
# print(f'concat is {len(transaction_detail)}')

# 003
join_data = pd.merge(
    transaction_detail, transaction[["transaction_id", "payment_date", "customer_id"]],
    on="transaction_id",
    how="left"
)
# print(join_data.head(5))
# print(f'detal is {len(transaction_detail)}')
# print(f'normal is {len(transaction)}')
# print(f'merged is {len(join_data)}')

# 004
join_data = pd.merge(
    join_data, customer_master,
    on="customer_id",
    how="left"
)
join_data = pd.merge(
    join_data, item_master,
    on="item_id",
    how="left"
)
# print(join_data.head(5))

# 005
join_data["price"] = join_data["quantity"] * join_data["item_price"]
print(join_data[["quantity", "item_price", "price"]].head(5))