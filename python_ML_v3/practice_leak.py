"""
20261115
交差検証とリーク防止デモ
例1: グループリーク（同じ顧客が学習と検証の両方に入る）
例2: 前処理リーク（特徴量選択をCVの外で全データに対して行う）
例3: 層化の効果（不均衡データでfoldごとの陽性数がぶれる）
"""
import numpy as np
from sklearn.model_selection import KFold, GroupKFold, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline

rng = np.random.default_rng(0)

# ---------- 例1: グループリーク ----------
# 100人の顧客 × 各10件の購買ログ。ラベルは「顧客ごと」に決まり、特徴量とは無関係（本当の実力はAUC 0.5）
n_users, per_user = 100, 10
groups = np.repeat(np.arange(n_users), per_user)
user_vec = rng.normal(size=(n_users, 5))          # 顧客固有のクセnm   b                          bv
X = user_vec[groups] + rng.normal(scale=0.1, size=(n_users * per_user, 5))
y = rng.integers(0, 2, n_users)[groups]

model = RandomForestClassifier(n_estimators=100, random_state=0)
auc_kf = cross_val_score(model, X, y, cv=KFold(5, shuffle=True, random_state=0), scoring="roc_auc")
auc_gkf = cross_val_score(model, X, y, cv=GroupKFold(5), groups=groups, scoring="roc_auc")
print("[例1] グループリーク（本当の実力は0.5）")
print(f"  KFold（同じ顧客が両側に入る） AUC = {auc_kf.mean():.3f}")
print(f"  GroupKFold（顧客単位で分割）  AUC = {auc_gkf.mean():.3f}")

# ---------- 例2: 前処理リーク ----------
# サンプル100件・特徴量5000個・すべて乱数。ラベルとは無関係（本当の実力は正解率0.5）
X2 = rng.normal(size=(100, 5000))
y2 = rng.integers(0, 2, 100)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

# NG: 全データでラベルを見て上位20特徴を選んでからCV
X2_sel = SelectKBest(f_classif, k=20).fit_transform(X2, y2)
acc_ng = cross_val_score(LogisticRegression(max_iter=1000), X2_sel, y2, cv=cv)
# OK: Pipelineに入れて、各foldの学習データだけで特徴選択
pipe = make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression(max_iter=1000))
acc_ok = cross_val_score(pipe, X2, y2, cv=cv)
print("[例2] 前処理リーク（本当の実力は0.5）")
print(f"  CVの外で特徴選択（NG）   正解率 = {acc_ng.mean():.3f}")
print(f"  Pipelineで各fold内（OK） 正解率 = {acc_ok.mean():.3f}")

# ---------- 例3: 層化の効果 ----------
y3 = np.array([1] * 20 + [0] * 980)   # 陽性2%
X3 = np.zeros((1000, 1))
kf_pos = [int(y3[va].sum()) for _, va in KFold(5, shuffle=True, random_state=1).split(X3)]
skf_pos = [int(y3[va].sum()) for _, va in StratifiedKFold(5, shuffle=True, random_state=1).split(X3, y3)]
print("[例3] 陽性2%のデータで、各foldの検証側に入る陽性の数")
print(f"  KFold           {kf_pos}")
print(f"  StratifiedKFold {skf_pos}")