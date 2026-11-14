"""
無向グラフ。
UnionFindを使ったときに、何が起きるんだ？？
例１だと、2-3のエッジが作られたことで、親子関係が壊れた、のか？
例２だと、4-1のエッジが作られたことで、親子関係が壊れた、のか？
UnionFindクラスでUnionして親ノードをそろえたうえで、、
parent,group_count,sizeで議論できるか？→できないな。

次元を管理すればいいのか？

１つずつエッジを追加していき、隣接行列を更新する。
もし、エッジを追加したときに、
既に次数が１だった場合に、そのエッジをリターンする。
※UnionFindは使わない

"""
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)+1
        dimentions = [[0] * n] * n
        for i,j in edges:
            dimentions[i][j] += 1
            if dimentions[i][j] > 1:
                return [i,j]
