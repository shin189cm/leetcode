# 011
import pandas as pd
from rich import print
uriage_data = pd.read_csv('uriage.csv')
# print(uriage_data.head())

kokyaku_data = pd.read_excel('kokyaku_daicho.xlsx')
# print(kokyaku_data.head())

# 012 表記が揺れている
# print(uriage_data["item_name"].head())
# print(uriage_data["item_price"].head())

# 013 商品数が多すぎる、表記ゆれに起因している
uriage_data["purchase_date"] = pd.to_datetime(uriage_data["purchase_date"])
uriage_data["purchase_month"] = uriage_data["purchase_date"].dt.strftime("%Y%m")
res = uriage_data.pivot_table(index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
# print(res)
res = uriage_data.pivot_table(index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
# print(res)

# 014 小文字→大文字、全角スペース消す、半角スペース消す
# print(len(pd.unique(uriage_data["item_name"])))
uriage_data["item_name"] = uriage_data["item_name"].str.upper()
uriage_data["item_name"] = uriage_data["item_name"].str.replace("　","")
uriage_data["item_name"] = uriage_data["item_name"].str.replace(" ","")
uriage_data.sort_values(by=["item_name"], ascending=True)
# print(uriage_data.head(10))
# print(pd.unique(uriage_data["item_name"]))
# print(len(pd.unique(uriage_data["item_name"])))

# 015 数値欠損の補完
# print(uriage_data.isnull().any(axis=0))
flg_is_null = uriage_data["item_price"].isnull()
# for trg in list(uriage_data.loc[flg_is_null, "item_name"].unique()):
#     price = uriage_data.loc[(~flg_is_null)&(uriage_data["item_name"]==trg), "item_price"].max()
#     uriage_data.loc[(flg_is_null)&(uriage_data["item_name"]==trg), "item_price"] = price

# 高速で簡潔な、標準的なアプローチ
uriage_data["item_price"] = uriage_data.groupby("item_name")["item_price"].transform(
    lambda x: x.fillna(x.dropna().max() if not x.dropna().empty else None)
)
# print(uriage_data.head(10))
# print(uriage_data.isnull().any(axis=0))
for trg in list(uriage_data["item_name"].sort_values().unique()):
    print(trg + "の最大額：" + str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].max()) + "/の最少額：" + str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].min(skipna=False)))

