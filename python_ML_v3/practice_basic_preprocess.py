import numpy as np, pandas as pd
from rich import print
# 東アジアの幅（全角文字）を考慮して表示位置を揃える
pd.set_option("display.unicode.east_asian_width", True)

# 事前のデータ作成
# rng = np.random.default_rng(42)
# n_cust = 200
# customer = pd.DataFrame({
#     "customer_id": [f"C{i:04d}" for i in range(n_cust)],
#     "gender": rng.choice(["M", "F"], n_cust),
#     "birth_date": pd.to_datetime("1960-01-01") + pd.to_timedelta(rng.integers(0, 365*45, n_cust), unit="D"),
#     "store_cd": rng.choice(["S01", "S02", "S03"], n_cust),
# })
# customer.loc[rng.choice(n_cust, 15, replace=False), "birth_date"] = pd.NaT
# n = 3000
# receipt = pd.DataFrame({
#     "sales_date": pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D"),
#     "customer_id": rng.choice(customer["customer_id"].iloc[:170], n),
#     "product_cd": rng.choice([f"P{i:03d}" for i in range(30)], n),
#     "amount": rng.integers(100, 8000, n).astype(float),
# })
# receipt.loc[rng.choice(n, 40, replace=False), "amount"] = np.nan
# customer.to_csv("customer.csv", index=False)
# receipt.to_csv("receipt.csv", index=False)


# トレーニング

# 読み込み
customer = pd.read_csv('customer.csv')
receipt = pd.read_csv('receipt.csv')
# print(customer.shape)
# print(customer.head())
# print(receipt.shape)
# print(receipt.head())
# print(receipt.dtypes)

# 1 金額ピックアップ
receipt["sales_date"] = pd.to_datetime(receipt["sales_date"])
# res_1 = receipt.loc[(receipt["sales_date"].between(pd.to_datetime("20250701"), pd.to_datetime("20250930")))] #誤答
res_1 = receipt.loc[
    (receipt["sales_date"].between(pd.to_datetime("20250701"), pd.to_datetime("20250930")))
    & (receipt["amount"] >= 1000)
    & (receipt["amount"] <= 5000)
    ]
# print("len: ",len(res_1))

# 2 顧客ごとに、売上の合計金額と購入回数（レシートの行数）を出してください。
# 合計金額の多い順に上位5人を、customer_id を列として残した表で示してください。
# groupbyして、aggfuncをsum, countにする
# sortする
# res_2 = receipt.groupby("customer_id", as_index=False)[["amount"]].agg(["sum", "size"]).sort_values(("amount", "sum"), ascending=False)
res_2 = receipt.groupby("customer_id", as_index=False).agg(total=("amount", "sum"), n=("amount", "size"))
# print(res_2.head(5))
# res_2_2 = res_2.sort_values(res_2[""])

# 3 顧客テーブルの全員に売上の合計金額を付けてください。
# 一度も買っていない顧客も残し、合計金額は0にします。全体の行数と、合計が0の顧客の人数を答えてください。
# print(res_2.columns)
res_3 = pd.merge(customer, res_2[["customer_id", "total"]], on="customer_id", how="left")
res_3["total"] = res_3["total"].fillna(value=0)
# print(res_3.head())
# print("全体の行数", len(res_3))
# print("合計が0の顧客人数", len(res_3.loc[res_3["total"] == 0]))
# (res_3["total"] == 0).sum()


# 4 年代（20代、30代…）×月の売上合計を、行が年代・列が月の表にしてください。
# 年齢は「2025 − 生まれた年」で計算してかまいません。生年月日が空の顧客は除きます。
cust_2 = customer.dropna(subset=["birth_date"]).copy()
cust_2["birth_date"] = pd.to_datetime(cust_2["birth_date"])
cust_2["age_group"] = 2025 - cust_2["birth_date"].dt.year
# res_3["age_group"] = (x//10 for x in res_3["age_group"])
cust_2["age_group"] = (cust_2["age_group"] // 10 * 10).astype('int')
# print(cust_2.head())
# print(receipt.head())
res_4 = pd.merge(receipt, cust_2[["customer_id", "age_group"]], on="customer_id", how="inner")# 誕生日のnanを防ぐ
res_4["sales_date"] = pd.to_datetime(res_4["sales_date"])
res_4["sales_month"] = res_4["sales_date"].dt.month
res_4 = res_4.pivot_table(index = "age_group", columns="sales_month", values="amount", aggfunc="sum")
print(res_4)

# 5 2025-12-31 を基準日として、顧客ごとに最後に買った日から何日たったかを出してください。
# 日数が最も大きい3人を答えてください。

# ここから
