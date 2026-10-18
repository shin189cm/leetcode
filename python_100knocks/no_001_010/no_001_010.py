# # 001
# import pandas as pd
# from rich import print
# import matplotlib.pyplot as plt

# customer_master = pd.read_csv('customer_master.csv', encoding='utf-8')
# # print(customer_master[0:5])
# item_master = pd.read_csv('item_master.csv', encoding='utf-8')
# transaction_1 = pd.read_csv('transaction_1.csv', encoding='utf-8')
# transaction_2 = pd.read_csv('transaction_2.csv', encoding='utf-8')
# transaction_detail_1 = pd.read_csv('transaction_detail_1.csv', encoding='utf-8')
# transaction_detail_2 = pd.read_csv('transaction_detail_2.csv', encoding='utf-8')

# # print(item_master.head(1))
# # print(transaction_1.head(1))
# # print(transaction_2.iloc[[0]])
# # print(transaction_detail_1.iloc[[0]])
# # print(transaction_detail_2.iloc[[0]])

# # 002
# transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
# # print(transaction.head(3))
# # print(f'1 is {len(transaction_1)}')
# # print(f'2 is {len(transaction_2)}')
# # print(f'concat is {len(transaction)}')

# transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
# # print(transaction_detail.head(3))
# # print(f'1 is {len(transaction_detail_1)}')
# # print(f'2 is {len(transaction_detail_2)}')
# # print(f'concat is {len(transaction_detail)}')

# # 003
# join_data = pd.merge(
#     transaction_detail, transaction[["transaction_id", "payment_date", "customer_id"]],
#     on="transaction_id",
#     how="left"
# )
# # print(join_data.head(5))
# # print(f'detal is {len(transaction_detail)}')
# # print(f'normal is {len(transaction)}')
# # print(f'merged is {len(join_data)}')

# # 004
# join_data = pd.merge(
#     join_data, customer_master,
#     on="customer_id",
#     how="left"
# )
# join_data = pd.merge(
#     join_data, item_master,
#     on="item_id",
#     how="left"
# )
# # print(join_data.head(5))

# # 005
# join_data["price"] = join_data["quantity"] * join_data["item_price"]
# # print(join_data[["quantity", "item_price", "price"]].head(5))

# # 006 検算
# # print(f'sum of join_data is\t{join_data["price"].sum()}')
# # print(f'sum of transaction is\t{transaction["price"].sum()}')
# # print(f'join_data : transaction is {join_data["price"].sum() == transaction["price"].sum()}')

# # 007 各統計量の確認。null
# # print(join_data.isnull().sum())
# # print(join_data.describe())
# # 数値以外の統計量のチェック
# # print(f'min of date is {join_data["payment_date"].min()}\nmax of date is {join_data["payment_date"].max()}')

# # 008
# # print(join_data.dtypes)
# join_data["payment_date"] = pd.to_datetime(join_data["payment_date"])
# join_data["payment_month"] = join_data["payment_date"].dt.strftime("%Y%m")
# # print(join_data[["payment_date", "payment_month"]].head())
# # print(join_data.groupby("payment_month").sum()["price"])

# # 009
# # print(join_data.groupby(["payment_month", "item_name"]).sum()[["price", "quantity"]])
# # print(pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price', 'quantity'], aggfunc='sum'))

# # 010
# graph_data = pd.pivot_table(join_data, index='payment_month', columns='item_name', values='price', aggfunc='sum')
# print(graph_data.head())
# # plt.plot(list(graph_data.index), graph_data["PC-A"], label='PC-A')
# # plt.plot(list(graph_data.index), graph_data["PC-B"], label='PC-B')
# # plt.plot(list(graph_data.index), graph_data["PC-C"], label='PC-C')
# # plt.plot(list(graph_data.index), graph_data["PC-D"], label='PC-D')
# # plt.plot(list(graph_data.index), graph_data["PC-E"], label='PC-E')
# # plt.legend()
# # plt.show()

# cols = ["PC-A", "PC-B", "PC-C", "PC-D", "PC-E"]
# graph_data[cols].plot()
# plt.show()

###

# 20261016復習
# 001
import pandas as pd
from rich import print
import matplotlib.pyplot as plt

customer_master = pd.read_csv('customer_master.csv')
# print(customer_master.head())

# 002
item_master = pd.read_csv('item_master.csv')
transaction_1 = pd.read_csv('transaction_1.csv')
transaction_2 = pd.read_csv('transaction_2.csv')
transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')

transaction = pd.concat([transaction_1, transaction_2], ignore_index=True) # ignore_indexで、indexを振りなおしている
# print(transaction.head())

transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
# print(transaction_detail.head())

# 003
join_data = pd.merge(transaction_detail, transaction[["transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")
# print(join_data.head())
# print(len(transaction_detail))
# print(len(transaction))
# print(len(join_data))

# 004
join_data = pd.merge(join_data, customer_master, on="customer_id", how="left")
join_data = pd.merge(join_data, item_master, on="item_id", how="left")
# print(join_data.head())

# 005
join_data["price"] = join_data["quantity"] * join_data["item_price"]
# print(join_data[["quantity", "item_price", "price"]].head())

# 006
# print(join_data["price"].sum())
# print(transaction["price"].sum())

# 007
# print(join_data.isnull().sum())
# print(join_data.describe())
# print(join_data["payment_date"].min()) # 数値データ以外をチェックする
# print(join_data["payment_date"].max())

# 008
# print(join_data.dtypes)
join_data["payment_date"] = pd.to_datetime(join_data["payment_date"])
join_data["payment_month"] = join_data["payment_date"].dt.to_period("M")
# join_data["payment_month"] = join_data["payment_date"].dt.strftime("%Y%m")
# print(join_data[["payment_date","payment_month"]].head())

# print(join_data.groupby("payment_month").sum()["price"])

# 009
# print(join_data.groupby(["payment_month","item_name"]).sum()[["price","quantity"]])
# print(pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price', 'quantity'], aggfunc='sum'))

# 010
graph_data = pd.pivot_table(join_data, index='payment_month', columns='item_name', values='price', aggfunc='sum')
# print(graph_data.head())
cols = ["PC-A", "PC-B", "PC-C", "PC-D", "PC-E"]
graph_data[cols].plot()
plt.show()