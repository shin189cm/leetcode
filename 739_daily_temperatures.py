"""Problem: 739_daily_temperatures.py

URL: https://leetcode.com/problems/daily-temperatures/
Difficulty: Medium
Category: Array, Stack, Monotonic Stack

Complexity:
- Time: O(N)
    - 配列の要素数を N とする。
    - 各インデックス i は、スタックに最大1回 push され、最大1回 pop される。
    - 外側の for ループは N 回実行され、内側の while ループによる pop 操作の総回数は
      走査全体を通じて高々 N 回であるため、償却計算量は O(N) となる。
- Space: O(N)
    - 最悪ケース（気温が厳密に降順に並んでいる場合など）において、
      すべてのインデックスがスタックに蓄積されるためスタックの空間量は O(N)。
    - 結果を返すための出力配列 res に O(N) を要する。

Approach:
1. 「Next Greater Element（次に大きい要素の探索）」問題への帰着
    - 単純な二重ループでは O(N^2) となり TLE となるため、未解決の要素をスタックで管理する。
2. 単調スタック（Monotonic Decreasing Stack）の構築
    - スタック内には「まだ自分より高い気温に遭遇していない日のインデックス」を保持する。
    - スタック内のインデックスに対応する気温は常に降順（または等しい）状態が維持される。
3. 走査と差分計算
    - 現在の日 i の気温 curr_temp について、スタック末尾の日の気温より高い間、以下を繰り返す：
        - スタックから前日のインデックス prev_i を pop する。
        - prev_i 日目から見た「次に暖かい日までの日数」は i - prev_i で確定するため、res[prev_i] に記録する。
    - 条件を満たさなくなったら、現在の日 i をスタックに push して次の日の走査へ進む。
4. 初期値の活用
    - 配列長 N を 0 で初期化した配列 res を用意しておくことで、最後までより暖かい日が現れず
      スタックに残った日については明示的な更新を行わずに 0 をそのまま返却できる。

memo:
- スタックに入れる要素は「気温そのもの」ではなく「インデックス」のみで十分（temperatures[idx] で値は引けるため、タプルで保持するオーバーヘッドを削減可能）。
- 後続の要素によって過去の要素が一斉に解消される構造を見たら、優先度付きキュー（Heap）の O(N log N) よりもまず単調スタックの O(N) を検討するのが定石。
"""


class Solution:

  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    res = [0] * n
    stack = []  # 格納するのはインデックスのみ

    for curr_idx, curr_temp in enumerate(temperatures):
      # スタック末尾の気温より現在の気温が高い間、過去の未決定要素を解消する
      while stack and temperatures[stack[-1]] < curr_temp:
        prev_idx = stack.pop()
        res[prev_idx] = curr_idx - prev_idx

      # 現在のインデックスをスタックに追加
      stack.append(curr_idx)

    return res
