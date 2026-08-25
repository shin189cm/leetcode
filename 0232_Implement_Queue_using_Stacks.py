"""
Problem: 0232_implement_queue_using_stacks.py
URL: https://leetcode.com/problems/implement-queue-using-stacks/
Difficulty: Easy
Category: Stack, Design, Queue

Complexity:
- Time:
  - push: O(1) - in_stack への末尾追加のみ
  - pop / peek: 償却 O(1) - 最悪時は in_stack から out_stack への全移動で O(N) だが、各要素の移動回数は高々2回のため
  - empty: O(1) - 両スタックの長さ判定のみ
- Space: O(N) - 保持する全要素数 N を2つのスタックで分散して保持するため

Approach:
1. 要素受け付け用の in_stack と、取り出し用の out_stack の2つのスタックを用意する。
2. push(x): in_stack に要素を append する。
3. pop() / peek():
   - out_stack が空の場合のみ、in_stack の全要素を pop して out_stack に append（順序を反転して FIFO を実現）。
   - out_stack の末尾（Top）から値を取り出す / 参照する。
4. empty(): in_stack と out_stack の両方が空であるか判定する。
"""

class MyQueue:

    def __init__(self):
        # 2つのスタックを用意
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # 要素の追加は in_stack の末尾へ
        self.in_stack.append(x)

    def pop(self) -> int:
        # out_stack に要素を準備してから末尾を取り出す
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        # out_stack に要素を準備してから末尾を参照する
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        # 両方のスタックが空なら Queue は空
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def _move(self) -> None:
        # out_stack が空の場合のみ、in_stack の全要素を移し替えて反転させる
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
