# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        BST。二分探索木。
        inorderで1次元配列に変換すると、昇順ソートになるはず。
        ん？min_heapに入れてしまえば？→TreeNode型なので難しい。
        inorderをして、順に貯めて行って、k番目の値を返せばいいのか。
        """
        if not root:
            return Flase
        
        res = []

        def inorder(self, node: TreeNode | None):
            if node != root:

            if not node.left and not node.right:

            

        """

        min_heap = heapq.heapify(root)

        while len(min_heap) < k:
            heapq.heappop(min_heap)

        min_heap = root
        heapq.heapify(root[:k])

        for idx, num in enumerate(root):
            if min_heap[0] > num:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]
        """
