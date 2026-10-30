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
# print(uselog.head())
# print(uselog.loc[uselog["customer_id"]=="AS002855"])
# print(year_months)


# 42
# 退会前月のCSデータをつくる
# 9月末退会者は、8月上旬には退会申請している。つまり7月の行動がキーのはずだ。
from dateutil.relativedelta import relativedelta
exit_customer = customer.loc[customer["is_deleted"]==1].copy()
# print(len(exit_customer))
exit_customer["exit_months"] = None
exit_customer["end_months"] = pd.PeriodIndex(exit_customer["end_date"], freq="M")
exit_customer["exit_months"] = exit_customer["end_months"] - 1
# print("exit_customer.head()")
# print(exit_customer[["end_date", "end_months", "exit_months"]].head())
exit_uselog = pd.merge(
    uselog,
    exit_customer,
    left_on=["customer_id", "年月"],
    right_on=["customer_id", "exit_months"],
    how="left",
    indicator=True # both, left_only, right_only
)
# print(len(uselog))
# print("exit_uselog.head()")
# print(exit_uselog.head())
# 欠損が多いため、欠損をdropする
exit_uselog = exit_uselog[exit_uselog["_merge"]=="both"] # both, left_only, right_only
exit_uselog = exit_uselog.drop(columns=["_merge"])
# print(len(exit_uselog))
# print(len(exit_uselog["customer_id"].unique()))
# print("exit_uselog.head()")
# print(exit_uselog.head())
# print(len(exit_uselog))


# 43
conti_customer = customer.loc[customer["is_deleted"] == 0]
conti_uselog = pd.merge(
    uselog,
    conti_customer,
    on=["customer_id"],
    how="left",
    indicator=True
)
# print(conti_uselog.head())
# print(len(conti_uselog))
conti_uselog = conti_uselog[conti_uselog["_merge"]=="both"]
conti_uselog = conti_uselog.drop(columns=["_merge"])
# print(len(conti_uselog))
# 多すぎる。ユーザー数と行動数が一対多。アンダーサンプリングする。退会者と同じ数にする。
conti_uselog = conti_uselog.sample(frac=1, random_state=0).reset_index(drop=True)
conti_uselog = conti_uselog.drop_duplicates(subset="customer_id")
# print(len(conti_uselog))
# print(conti_uselog.head())
# print("exit_uselog.shape")
# print(exit_uselog.shape)
# print("conti_uselog.shape")
# print(conti_uselog.shape)
predict_data= pd.concat([conti_uselog, exit_uselog], ignore_index=True)
# print(predict_data.shape)
# print(predict_data.head())


# 44
# 説明変数に、在籍期間を入れたい
predict_data["period"] = None # ここに在籍月数を入れる
# print(predict_data["年月"].dtype)
predict_data["now_date"] = predict_data["年月"]
# print(f"shapeは {predict_data.shape}")
# print(predict_data["start_date"].dtype)
predict_data["start_date"] = pd.PeriodIndex(predict_data["start_date"], freq="M")
predict_data["period"] = predict_data["now_date"] - predict_data["start_date"]
predict_data["period"] = predict_data["period"].apply(lambda x: x.n) # DateOffset型をintに変換する
print(predict_data.head())


# 45