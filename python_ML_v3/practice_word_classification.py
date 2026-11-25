import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from rich import print
# 東アジアの幅（全角文字）を考慮して表示位置を揃える
pd.set_option("display.unicode.east_asian_width", True)

# 元データ
X_train = ["映画 面白い", "映画 楽しい 最高", "音楽 面白い", "音楽 最高", "ドラマ 楽しい",
           "映画 退屈", "映画 つまらない 最悪", "音楽 退屈", "音楽 最悪", "ドラマ つまらない"]
y_train = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]   # 1 = 好評、0 = 不評

X_test = ["ドラマ 最高", "映画 退屈 最悪", "アニメ 楽しい", "アニメ すばらしい"]

# 前処理
tfidf = TfidfVectorizer()

X_train_tfidf = tfidf.fit_transform(X_train)
# print(X_train_tfidf)
# print("行数は文章数、列数は、単語数かな")
# print(X_train_tfidf.shape)
# print(tfidf.get_feature_names_out())
# # print(X_train_tfidf.toarray())
# print(pd.DataFrame(X_train_tfidf.toarray(), columns=tfidf.get_feature_names_out()))

# print("アニメ 素晴らしい は、アニメがそもそもなくて、素晴らしいが1に近い値になるはずだ")
X_test_tfidf = tfidf.transform(X_test)
# print(pd.DataFrame(X_test_tfidf.toarray(), index=X_test, columns=tfidf.get_feature_names_out()))
# print("アニメ 素晴らしい は、アニメも、素晴らしいも、そもそもなかった。")

# 分類器を作る
clf = LogisticRegression()
clf.fit(X_train_tfidf, y_train)

print("切片： ", clf.intercept_)
print("予測： ", clf.predict(X_test_tfidf))
print("確率： \n", clf.predict_proba(X_test_tfidf).round(3))

# パイプラインの構築
pipe = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression()),
])

pipe.fit(X_train, y_train)
print("----------")
print(pipe.predict(X_test))
print(pipe.predict_proba(X_test))
