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
# 教科書のアプローチ
# for trg in list(uriage_data.loc[flg_is_null, "item_name"].unique()):
#     price = uriage_data.loc[(~flg_is_null)&(uriage_data["item_name"]==trg), "item_price"].max()
#     uriage_data.loc[(flg_is_null)&(uriage_data["item_name"]==trg), "item_price"] = price

# 高速で簡潔な、標準的なアプローチ
uriage_data["item_price"] = uriage_data.groupby("item_name")["item_price"].transform(
    lambda x: x.fillna(x.dropna().max() if not x.dropna().empty else None)
)
# print(uriage_data.head(10))
# print(uriage_data.isnull().any(axis=0))
# for trg in list(uriage_data["item_name"].sort_values().unique()):
#     print(trg + "の最大額：" + str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].max()) + "/の最少額：" + str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].min(skipna=False)))

# 016 名前の表記ゆれを修正する
# print(kokyaku_data["顧客名"].head())
# print(uriage_data["customer_name"].head())
kokyaku_data["顧客名"] = kokyaku_data["顧客名"].str.replace("　","")
kokyaku_data["顧客名"] = kokyaku_data["顧客名"].str.replace(" ","")
# print(kokyaku_data["顧客名"].head())

# 017 DATEの表記ゆれを修正する
flg_is_serial = kokyaku_data["登録日"].astype("str").str.isdigit()
# print(f'sum is {flg_is_serial.sum()}')
fromSerial = pd.to_timedelta(kokyaku_data.loc[flg_is_serial, "登録日"].astype("float")-2, unit="D") + pd.to_datetime('1900/1/1')
# print(fromSerial)
fromString = pd.to_datetime(kokyaku_data.loc[~flg_is_serial, "登録日"])
# print(fromString)
kokyaku_data["登録日"] = pd.concat([fromSerial, fromString])
# print(kokyaku_data)
kokyaku_data["登録年月"] = kokyaku_data["登録日"].dt.strftime("%Y%m")
rslt = kokyaku_data.groupby("登録年月").count()["顧客名"]
# print(f'len(kokyaku_data) is {len(kokyaku_data)}')
# print(rslt)
flg_is_serial = kokyaku_data["登録日"].astype("str").str.isdigit()
# print(flg_is_serial.sum())

# 018
join_data = pd.merge(uriage_data, kokyaku_data, 
                     left_on="customer_name",
                     right_on="顧客名", how="left")
join_data = join_data.drop("customer_name", axis=1)
# print(join_data)

# 019
dump_data = join_data[["purchase_date", "purchase_month", "item_name", "item_price", "顧客名", "かな", "地域", "メールアドレス", "登録日"]]
# print(dump_data)
dump_data.to_csv("dump_data.csv", index=False)

# 020
import_data = pd.read_csv("dump_data.csv")
# print(import_data)
byItem = import_data.pivot_table(index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
# print(byItem)
byPrice = import_data.pivot_table(index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
# print(byPrice)
byCustomer = import_data.pivot_table(index="purchase_month", columns="顧客名", aggfunc="size", fill_value=0)
# print(byCustomer)
byRegion = import_data.pivot_table(index="purchase_month", columns="地域", aggfunc="size", fill_value=0)
# print(byRegion)
away_data = pd.merge(uriage_data, kokyaku_data, left_on="customer_name", right_on = "顧客名", how="right")
print(away_data[away_data["purchase_date"].isnull()][["顧客名", "メールアドレス", "登録日"]])
