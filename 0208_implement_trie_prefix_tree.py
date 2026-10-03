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
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
