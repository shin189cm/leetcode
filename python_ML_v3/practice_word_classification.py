import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
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
print(X_train_tfidf)
print("行数は文章数、列数は、単語数かな")
print(X_train_tfidf.shape)
print(tfidf.get_feature_names_out())
# print(X_train_tfidf.toarray())
print(pd.DataFrame(X_train_tfidf.toarray(), columns=tfidf.get_feature_names_out()))
