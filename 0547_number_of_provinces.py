"""
nxn行列が与えられる。
座標の要素が1の場合、座標同士が直接つながっている。
provinceは、間接的につながっていても1つの集合体とみなす。

方針は、dfsかbfsで、訪問済みを管理しながら、数を特定することか。
最初に1の座標を抽出しておいて、queueに入れておいて、
それを順番に進めていくか。
その場合、
別々の開始点から動いたが同一のprovinceだった場合にどうする？
→1つとして扱いたい

上記の「最初に１を抽出する」方法をやめよう。
左上の座標00から2重ループを走査しよう。走査したら、逐一、訪問済みノード処理をしよう。
（0で塗り替えるのがわかりよいか。
もし、1だった場合、while queue：4方向の隣接セルに走査を続ける、訪問済みにする、、、、
走査終了後、result += 1する
もし、右下のセルに到達したら、終了

注意で、isConnectedが0か1かで返さなければならない。座標じゃなくて、接続関係。

"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        DIREC = ((1,0), (-1,0), (0,1), (0,-1))
        queue = []
        for i in range(n):
            for j in range(i,n):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0 # 訪問済み、塗り替える
                    queue.append(j) # jを起点に探す
                    while queue: # 起点がある限り
                        curr_j = queue.pop()
                        for nj in range(n):
                            if isConnected[curr_j][nj] == 1:
                                isConnected[curr_j][nj] = 0 # 訪問済み
                                queue.append(nj)
                    res += 1
        return res
