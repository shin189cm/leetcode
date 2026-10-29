import pandas as pd
from rich import print
import matplotlib.pyplot as plt
# 東アジアの幅（全角文字）を考慮して表示位置を揃える
pd.set_option("display.unicode.east_asian_width", True)

# 41
# データ読み込み整形する
customer = pd.read_csv("customer_join.csv")
uselog_months = pd.read_csv("use_log_months.csv")
# print("customer.head()")
# print(customer.head())
# print("uselog_months.head()")
# print(uselog_months.head())
# 過去1か月で当月の退会を予測する
year_months = sorted(uselog_months["年月"].unique())
# uselog = pd.DataFrame()
# for i in range(1, len(year_months)):
#     tmp = uselog_months.loc[uselog_months["年月"] == year_months[i]].copy()
#     tmp.rename(columns={"count":"count_0"}, inplace=True)
#     tmp_before = uselog_months.loc[uselog_months["年月"] == year_months[i-1]].copy()
#     del tmp_before["年月"]
#     tmp_before.rename(columns={"count":"count_0"}, inplace=True)
#     tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
#     uselog = pd.concat([uselog, tmp], ignore_index=True)
# print("uselog.head()")
# print(uselog.head())

tmp = uselog_months.copy()
tmp["年月"] = pd.PeriodIndex(tmp["年月"], freq="M")
tmp_prev = tmp[["customer_id", "年月", "count"]].copy()
tmp_prev["年月"] = tmp_prev["年月"] + 1# 過去データを未来へスライドさせる
tmp_prev.rename(columns={"count": "count_1"}, inplace=True)

uselog = pd.merge(
    tmp.rename(columns={"count": "count_0"}),
    tmp_prev,
    on=["customer_id", "年月"],
    how="left"
)
uselog = uselog[uselog["年月"] != pd.Period("2018-04", freq="M")]
# uselog = uselog[uselog["年月"] != "2018-04"]
print(uselog.head())
# print(uselog.loc[uselog["customer_id"]=="AS002855"])
# print(year_months)


# 42
# 退会前月のCSデータをつくる
