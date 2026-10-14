"""Problem: 146_lru_cache.py

URL: https://leetcode.com/problems/lru-cache/
Difficulty: Medium
Category: Hash Table, Linked List, Doubly-Linked List, Design

Complexity:
- Time:
    - __init__: O(1)
    - get: O(1)
        - ハッシュマップによるキー探索は平均 O(1)
        - ノードの参照を取得後、双方向連結リストからの切り離し・末尾への再挿入はポインタの繋ぎ替えのみで O(1)
    - put: O(1)
        - 既存キーの更新・末尾移動は O(1)
        - 新規追加時のノード作成、末尾挿入、マップ登録は O(1)
        - キャパシティ超過時の最古ノード（head.next）の削除およびマップからの破棄も O(1)
- Space: O(capacity)
    - ハッシュマップおよび双方向連結リスト内に保持されるエントリ数は最大で capacity 個
    - 各ノードは key, val, prev, next の定数個のポインタ・値を保持するため O(capacity)

Approach:
1. データ構造の選定
    - キャッシュの参照・更新を O(1) で行うため、キーとノード参照を紐付けるハッシュマップを採用する
    - キャッシュの利用順（LRU順）を O(1) で維持するため、双方向連結リスト（Doubly Linked List）を採用する
2. 番兵ノード（Sentinel Nodes）の導入
    - リストの両端に dummy head と dummy tail を配置する
    - head.next を「最も古く参照されたノード（Least Recently Used）」、tail.prev を「最も新しく参照されたノード」と定義する
    - これにより、要素数が 0 や 1 の場合の境界値処理（None チェック）を完全に排除し、安全にノードの挿入・削除を行う
3. 操作ロジックの分離
    - ノードの切り離し `_remove(node)` と末尾（tail 直前）への追加 `_add_to_tail(node)` をヘルパー関数として共通化する
    - get(key):
        - キーが存在しなければ -1 を返却
        - 存在すればノードを最新化（切り離して末尾へ移動）し、値を返却
    - put(key, value):
        - 既にキーが存在する場合は値を上書きし、最新化
        - 新規キーの場合、容量上限に達していれば head.next（最古ノード）をリストおよびマップから削除
        - 新規ノードを末尾に追加し、マップに登録

memo:
- Python 標準ライブラリの `collections.OrderedDict` を使用すれば数行で解ける（popitem(last=False) や move_to_end）
- しかしコーディングテストや技術面接では、背後にある「Hash Table + Doubly Linked List」の協調動作や
  ポインタ操作の正確性、番兵ノードの設計意図を問われるケースが大半であるため、プリミティブな実装が書けることが前提となる
"""

class ListNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> ListNode

        # 番兵ノード（ダミーノード）の初期化
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        """指定されたノードを双方向連結リストから切り離す"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: ListNode) -> None:
        """指定されたノードをリストの末尾（tail の直前）に挿入する"""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def _make_recently_used(self, node: ListNode) -> None:
        """ノードを一度切り離し、最新位置（末尾）へ再挿入する"""
        self._remove(node)
        self._add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._make_recently_used(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._make_recently_used(node)
            return

        if len(self.cache) >= self.capacity:
            # head.next は最古（LRU）のノード
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]

        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self._add_to_tail(new_node)
