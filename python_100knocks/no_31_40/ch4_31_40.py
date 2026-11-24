# import pandas as pd
# from rich import print
# import matplotlib.pyplot as plt
# # 東アジアの幅（全角文字）を考慮して表示位置を揃える
# pd.set_option("display.unicode.east_asian_width", True)


# # 31
# # データの中身を見る
# uselog = pd.read_csv('use_log.csv')
# # print(use_log.isnull().sum())

# customer = pd.read_csv("customer_join.csv")
# # print(customer.isnull().sum())


# # 32
# # 教師なし学習のkmeans
# customer_clustering = customer[["mean", "median", "max", "min", "membership_period"]]
# # print(customer_clustering.head())
# # 標準化
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler() # インスタンス化
# customer_clustering_sc = sc.fit_transform(customer_clustering)

# kmeans = KMeans(n_clusters = 4, random_state = 0) # インスタンス化
# clusters = kmeans.fit(customer_clustering_sc) # 最適化の実行
# customer_clustering = customer_clustering.assign(cluster = clusters.labels_) # メソッドチェーン的なassignの使い方

# # print(customer_clustering["cluster"].unique())
# # print(customer_clustering.head())
# # print(customer_clustering.groupby("cluster").mean())


# # 33
# # 結果を分析する
# # 列名を日本語にする
# customer_clustering.columns = ["月内平均値", "月内中央値", "月内最大値", "月内最小値", "会員期間", "cluster"]
# # print(customer_clustering.groupby("cluster").count())
# # print(customer_clustering.groupby("cluster").mean().round(2))


# # 34
# # クラスタリング結果を可視化する
# # PCAで次元削除する
# # from sklearn.decomposition import PCA
# # X = customer_clustering_sc
# # pca = PCA(n_components=2) # インスタンス化
# # pca.fit(X) # 最適化実施
# # x_pca = pca.transform(X) # 最適化を使って主成分化
# # pca_df = pd.DataFrame(x_pca)
# # pca_df["cluster"] = customer_clustering["cluster"]

# # for i in customer_clustering["cluster"].unique():
# #     tmp = pca_df[pca_df["cluster"]== i]
# #     plt.scatter(tmp[0], tmp[1],s=10)
# # plt.show()


# # 35
# # 顧客のグルーピングはできた。退会顧客の傾向を把握したい。
# customer_clustering = pd.concat([customer_clustering, customer], axis=1)
# # print(customer_clustering[["cluster", "is_deleted", "customer_id"]].groupby(["cluster", "is_deleted"], as_index=False).count())
# # print(customer.head())
# # print(customer_clustering.columns)
# # print(
# #     customer_clustering[["cluster", "routine_flg", "customer_id"]].groupby(["cluster", "routine_flg"], as_index=False).count()
# # )


# # 36
# # 予測する
# # 目的関数yは数値。教師あり学習の回帰となる。
# uselog["usedate"] = pd.to_datetime(uselog["usedate"])
# uselog["年月"] = uselog["usedate"].dt.to_period("M")
# uselog_months = uselog.groupby(["年月", "customer_id"], as_index=False).count()
# uselog_months.rename(columns={"log_id":"count"}, inplace=True)
# del uselog_months["usedate"]
# # print(uselog_months.head())

# year_months = sorted(uselog_months["年月"].unique())
# # print(year_months)
# predict_data = pd.DataFrame()
# for i in range(6, len(year_months)):
#     tmp = uselog_months.loc[uselog_months["年月"] == year_months[i]].copy()
#     tmp.rename(columns={"count":"count_pred"}, inplace=True)
#     for j in range(1, 7):
#         tmp_before = uselog_months.loc[uselog_months["年月"] == year_months[i-j]].copy()
#         del tmp_before["年月"]
#         tmp_before.rename(columns={"count":f"count_{j-1}"}, inplace=True)
#         tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
#     predict_data = pd.concat([predict_data, tmp], ignore_index=True)
# # print(predict_data.head())
# # 欠損値を削除する
# predict_data = predict_data.dropna()
# predict_data = predict_data.reset_index(drop=True)

# # 37
# # 特徴量を付与する
# predict_data = pd.merge(predict_data, customer[["customer_id", "start_date"]], on="customer_id", how="left")
# # print(predict_data.head())

# # print(predict_data["年月"].dtype)
# predict_data["now_date"] = predict_data["年月"].dt.to_timestamp()
# # print(predict_data.head())
# predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
# from dateutil.relativedelta import relativedelta
# predict_data["period"] = None
# # for i in range(len(predict_data)):
# #     delta = relativedelta(predict_data.loc[i, "now_date"], predict_data.loc[i, "start_date"])
# #     predict_data.loc[i, "period"] = delta.years * 12 + delta.months
# predict_data["period"] = (
#     (predict_data["now_date"].dt.year - predict_data["start_date"].dt.year) * 12
#     + (predict_data["now_date"].dt.month - predict_data["start_date"].dt.month)
# )
# # print(predict_data.head())
# # print(predict_data.isna().sum())


# # 38
# # ついに予測モデルを作成する。来月の利用回数を知りたい。
# predict_data = predict_data.loc[predict_data["start_date"] >= pd.to_datetime("20180401")]
# from sklearn import linear_model
# import sklearn.model_selection
# model = linear_model.LinearRegression()
# X = predict_data[["count_0", "count_1", "count_2", "count_3", "count_4", "count_5", "period"]]
# y = predict_data["count_pred"]
# # 指定なしのため、training vs. validation は 75% vs. 25% になる
# X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=0)
# model.fit(X_train, y_train)
# # print(model.score(X_train, y_train))
# # print(model.score(X_test, y_test))


# # 39
# coef = pd.DataFrame(
#     {"feature_names":X.columns,
#      "coefficient":model.coef_}
# )
# # print(coef)
# # 直近ジムに通っている回数が、最も効いているんだな。


# # 40
# # 予測用のダミーデータ
# x1 = [3,4,4,6,8,7,8]
# x2 = [2,2,3,3,4,6,8]
# x_pred = pd.DataFrame(data=[x1, x2], columns=["count_0", "count_1", "count_2", "count_3", "count_4", "count_5", "period"])
# print(model.predict(x_pred))

# uselog_months.to_csv("use_log_months.csv", index=False)



# 復習 --------------------------------------------------------------------------------
import pandas as pd
from rich import print
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 東アジアの幅（全角文字）を考慮して表示位置を揃える
pd.set_option("display.unicode.east_asian_width", True)

# 31
uselog = pd.read_csv('use_log.csv')
customer = pd.read_csv('customer_join.csv')

# print(uselog.isna().sum())
# print(customer.isna().sum())


# 32 クラスタリングする
customer_clustering = customer[["mean", "median", "max", "min", "membership_period"]]
# print(customer_clustering.head())

sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering) # fit（平均と標準偏差を覚える）もtransform（その値で変換）もする

kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(customer_clustering_sc)
customer_clustering = customer_clustering.assign(cluster = kmeans.labels_)

# print(customer_clustering["cluster"].unique())
# print(customer_clustering.head())


# 33 クラスタごとの概要
print(customer_clustering.groupby("cluster", as_index=False).agg(
    size=("cluster", "size"), 
    mean=("mean", "mean"),
    median=("median", "mean"),
    max=("max", "mean"),
    min=("min", "mean"),
    membership_period=("membership_period", "mean"))
    )


# 34
from sklearn.decomposition import PCA
X = customer_clustering_sc
pca = PCA(n_components=2)
pca.fit(X) # μとσを暗記する
x_pca = pca.transform(X) # 暗記したμとσで標準化する
pca_df = pd.DataFrame(x_pca)
pca_df["cluster"] = customer_clustering["cluster"]
# print(pca_df.head())

# for i in range(4):
#     tmp = pca_df.loc[pca_df["cluster"] == i]
#     plt.scatter(tmp[0], tmp[1])
# plt.show()


# 35 クラスタリング結果をもとに、退会顧客の傾向を探る
# print(customer.columns)
# print(customer_clustering.head())
# customer_clustering = pd.merge(customer_clustering, customer[["customer_id", "is_deleted"]], on="customer_id", how="left")
# indexで紐づけできるので、mergeではなく、concatで結合できる。
customer_clustering = pd.concat([customer_clustering, customer], axis=1)
# print(
#     customer_clustering.groupby(["cluster", "is_deleted"], as_index=False).count()[["cluster", "is_deleted", "customer_id"]]
# )


# 36 
# print(uselog.dtypes)
uselog["usedate"] = pd.to_datetime(uselog["usedate"])
uselog["年月"] = uselog["usedate"].dt.to_period("M")
# print(uselog.pivot_table(index="年月", columns="customer_id", aggfunc="count"))
uselog_month = uselog.groupby(["年月", "customer_id"], as_index=False).agg(count=("customer_id", "count"))
print(uselog_month.head())

month_list = sorted(uselog_month["年月"].unique())
tables = []
# print(month_list)
for i in range(6, len(month_list)):
    curr_month = month_list[i]
    temp = uselog_month.loc[uselog_month["年月"] == curr_month]
    for j in range(1,7):
        past = uselog_month.loc[uselog_month["年月"] == curr_month - j][["customer_id", "count"]]
        past = past.rename(columns={"count": f"count_{j}"})
        temp = pd.merge(temp, 
                        past, 
                        on=["customer_id"], how="left")
    tables.append(temp)
predict_data = pd.concat(tables, ignore_index=True)
print(predict_data.head())
# shitでの書き方もある。


# 次回はここから。
# 37
