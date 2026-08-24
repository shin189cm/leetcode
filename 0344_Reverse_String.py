from typing import List

class Solution:

  def reverseString(self, s: List[str]) -> None:
    """双ポインタ（Two Pointers）法を用いて文字列の配列をインプレースで反転する。

    両端（先頭と末尾）から中央に向かってポインタを進めながら、
    要素を順次スワップ（交換）して反転を実現する。

    Args:
        s (List[str]): 反転対象となる1文字ごとの文字列リスト。

    Returns:
        None: 返り値はなし。引数として渡されたリスト `s` を直接変更する。

    Complexity:
        - 時間計算量: O(N)
          リスト長 N に対し、N / 2 回のスワップ処理を行う。
        - 空間計算量: O(1)
          2つのポインタ変数（left, right）のみを使用し、追加のメモリ領域を消費しない。
    """
    left, right = 0, len(s) - 1

    while left < right:
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
