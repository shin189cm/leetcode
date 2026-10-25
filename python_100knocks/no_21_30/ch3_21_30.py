# 21
import pandas as pd
# 東アジアの幅（全角文字）を考慮して表示位置を揃える
pd.set_option("display.unicode.east_asian_width", True)


uselog = pd.read_csv('use_log.csv')
# print(len(uselog))
# print(uselog.head())

customer = pd.read_csv('customer_master.csv')
# print(len(customer))
# print(customer.head())

class_master = pd.read_csv('class_master.csv')
# print(len(class_master))
# print(class_master.head())

campaign_master = pd.read_csv('campaign_master.csv')
# print(len(campaign_master))
# print(campaign_master.head())


# 22
customer_join = pd.merge(customer, class_master, on="class", how="left")
customer_join = pd.merge(customer_join, campaign_master, on="campaign_id", how="left")
# print(customer_join.head())

# print(len(customer))
# print(len(customer_join))
# print(customer_join.isnull().sum())


# 23
# print(customer_join.groupby("class_name").count()["customer_id"])
# print(customer_join.groupby("campaign_name").count()["customer_id"])
# print(customer_join.groupby("gender").count()["customer_id"])
# print(customer_join.groupby("is_deleted").count()["customer_id"])

customer_join["start_date"] = pd.to_datetime(customer_join["start_date"])
customer_start = customer_join.loc[customer_join["start_date"] > pd.to_datetime("20180401")]
# print(len(customer_start))


# 24
customer_join["end_date"] = pd.to_datetime(customer_join["end_date"])
customer_newer = customer_join.loc[
    (customer_join["end_date"] >= pd.to_datetime("20190331"))
    | (customer_join["end_date"].isna())
]
# print(len(customer_newer))
# print(customer_newer["end_date"].unique())
# print(customer_newer.groupby("class_name").count()["customer_id"])
# print(customer_newer.groupby("campaign_name").count()["customer_id"])
# print(customer_newer[["customer_id", "campaign_name"]].groupby("campaign_name").count())
# print(customer_newer[["campaign_name"]].value_counts())
# print(customer_newer[["campaign_name"]].value_counts(normalize=True))
# print(customer_newer.groupby("campaign_name").count()["customer_id"] / len(customer_newer))
# print(customer_newer.groupby("gender").count()["customer_id"])


# 25
uselog["usedate"] = pd.to_datetime(uselog["usedate"])
uselog["年月"] = uselog["usedate"].dt.to_period("M")
uselog_months = uselog.groupby(["年月", "customer_id"], as_index=False).count()
# print(uselog_months.head())
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]
# print(uselog_months.head())

uselog_customer = uselog_months.groupby("customer_id").agg(["mean", "median", "max", "min"])["count"]
uselog_customer = uselog_customer.reset_index(drop=False)
# print(uselog_customer.head())


# 26
uselog["weekday"] = uselog["usedate"].dt.weekday
uselog_weekday = uselog[["customer_id", "年月", "weekday", "log_id"]].groupby(["customer_id", "年月", "weekday"], as_index=False).count()
uselog_weekday.rename(columns={"log_id":"count"}, inplace=True)
print(uselog_weekday.head(20))