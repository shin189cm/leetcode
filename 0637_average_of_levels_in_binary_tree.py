# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        """
        TreeNodeオブジェクト。
        BFSで層管理して計算する。
        長さをとって、単一のqueueで管理する。
        結果格納用のresと、都度その層の格納用の配列が必要。
        時間計算量は、全ノードをqueueに格納し、1回ずつ加算する。層ごとに1回割り算する。よってO(N)
        空間計算量は、最もノードが多い層が最大。最大約N/2。よってO(N)
        """
        if not root:
            return []

        queue = deque([root])
        res = [root.val] # floatを層数ぶん格納する
        current = []
        len_curr = 0

        while queue:
            current = []
            len_curr = 0
            # 中身がある間は続ける
            for i in range(len(queue)):
                # 取り出す
                curr = queue.popleft()
                # 値を格納する
                if curr.left:
                    queue.append(curr.left)
                    current.append(curr.left.val)
                    len_curr += 1
                if curr.right:
                    queue.append(curr.right)
                    current.append(curr.right.val)
                    len_curr += 1
            ave_curr = sum(current) / len_curr
            res.append(ave_curr)

        return res
