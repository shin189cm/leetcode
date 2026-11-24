import pandas as pd
from rich import print
# 東アジアの幅（全角文字）を考慮して表示位置を揃える
pd.set_option("display.unicode.east_asian_width", True)

# Q1（groupby）：次の df から、顧客ごとの「合計金額」と「購入回数」を出してください。
df = pd.DataFrame({
    "customer_id": ["A", "B", "A", "C", "B", "A"],
    "amount":      [1000, 500, 2000, 800, 1500, 300],
})
summary = df.groupby("customer_id", as_index=False).agg(total = ("amount", "sum"), n=("amount", "size"))
print(summary.head())

# Q2（merge）：次の customers に、Q1の結果をつなげてください。
customers = pd.DataFrame({
    "customer_id": ["A", "B", "C", "D"],
    "name":        ["佐藤", "鈴木", "高橋", "田中"],
})
customer_join = (
    pd.merge(customers, summary, on="customer_id", how="left")
        .fillna({"total": 0, "n": 0})
        .astype({"n": int})
    )
print(customer_join)
