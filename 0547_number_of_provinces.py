class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        直接繋がっていなくても、cityが繋がりのあるまとまりになっていれば、province.
        adjacent matrix
        provinceの数をreturnしよう。
        """
        def __init__(self, x: int, n: int):
            self.parent[x] = [1] * n
            self.group_num = n
        
        def parent(self, ):
            if self.parent(x) != x:
                self.parent(x) = self.parent(self.find(x))

        def union(self, root_x: int, root_y: int):
            if self.size(root_x) < self.size(root_y):
                root_x, root_y = root_y, root_x
