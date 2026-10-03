"""Problem: 208_implement_trie_prefix_tree.py

URL: https://leetcode.com/problems/implement-trie-prefix-tree/
Difficulty: Medium
Category: Data Structure, Trie, Design

Complexity:
- Time:
    - insert(word): O(L)
        - 単語の長さ L 回分、ノードの存在確認と生成を繰り返す。辞書のキー探索および生成は平均 O(1)
    - search(word): O(L)
        - 単語の長さ L 回分、木の子ノードを辿る。終端フラグの確認は O(1)
    - startsWith(prefix): O(L)
        - 接頭辞の長さ L 回分、木の子ノードを辿る。全て存在すれば True
- Space: O(T)
    - T を挿入された全文字列の総文字数とする。
    - 最悪の場合（共通接頭辞が存在しない場合）、文字数分の TrieNode が作成される。
    - 各ノードは子ノード参照用の辞書（英小文字26文字分）と bool 値を保持するため、O(T * |Sigma|)（|Sigma| = 26）。

Approach:
1. TrieNode クラスの定義
    - 各ノードに children（辞書: 文字 -> TrieNode）と is_end（単語の終端を示す bool）を持たせる。
2. insert 操作
    - ルートノードから開始し、各文字について children に存在しなければノードを新規作成して移動。
    - 単語の最後の文字に対応するノードの is_end を True に更新。
3. search / startsWith 操作
    - ルートから接頭辞の各文字を辿る。途中でノードが存在しなければ False。
    - startsWith は最後まで辿り着ければ直ちに True。
    - search は最後まで辿り着いた上で、そのノードの is_end が True であるかを確認して判定。

memo:
- 文字列のリスト保持による線形探索（O(N * L)）を、プレフィックス木構造を用いることで
  単語数 N に依存しない O(L) の高速な検索に落とし込む典型問題。
- 実装方法としては TrieNode クラスを分ける方法と、ネストした辞書（dict）のみで表現する軽量な方法があるが、
  オブジェクト指向設計の明確さ・拡張性の観点からクラス分離型が面接では推奨される。
"""

# 追加のクラスの定義
class TrieNode:
    def __init__(self):
        self.children = {} # 属性の作成。空の辞書。次の1文字をkeyとし、遷移先となる次のTrieNodeインスタンスを値とする。
        self.is_end = False # 属性の作成。ノードが単語の終わり（末尾）であることを表すフラグ。


class Trie:

    def __init__(self):
        self.root = TrieNode() # 属性の作成。TrieNodeクラスのインスタンス化。生成された実体（オブジェクト）の代入。

    def insert(self, word: str) -> None:
        curr = self.root # __init__で生成されたself.rootインスタンスへの参照を、変数に代入。
        # 探索の現在地を表すポインタの初期化。木構造の根（rootノードのインスタンス）への参照を代入。
        
        for char in word: # 1文字ずつ走査
            if char not in curr.children: # もし現在のNodeの子にその文字が無ければ
                curr.children[char] = TrieNode() # インスタンス生成して辞書登録する
            curr = curr.children[char] # 現在地currを、その文字に対応する子Nodeへ進める
        curr.is_end = True # 全文字終了時点で、最終的な到達点のNodeのis_end属性の値をTrueにする

    def search(self, word: str) -> bool:
        curr = self.root # 現在地currのポインタの初期化。
        for char in word: # 1文字ずつ走査
            if char not in curr.children: # もし、走査中の1文字が、子Nodeに含まれていない場合
                return False # Falseを返す
            curr = curr.children[char] # 現在地currを、走査中の1文字に対応する子Nodeへ進める
        return curr.is_end # 全文字終了後、wordの最終文字の属性is_endの値を返す。ちょうど単語の終わりか判定する。

    def startsWith(self, prefix: str) -> bool:
        curr = self.root # 現在地currのポインタの初期化
        for char in prefix: # 1文字ずつ走査
            if char not in curr.children: # 走査中の1文字が子Nodeに含まれていない場合
                return False # その接頭辞を持つ単語は存在しないためFalse
            curr = curr.children[char] # 現在地currを次の文字の子Nodeへ進める
        return True # 全文字辿り着けた時点で、その接頭辞を持つ単語が存在することが確定するためTrue

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
