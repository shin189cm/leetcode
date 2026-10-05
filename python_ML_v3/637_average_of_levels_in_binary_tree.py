# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        """
        同じレイヤーの平均値を求められている。
        要求精度は10^-5の誤差まで。
        TreeNodeクラスを使える。
        おそらくBFSの問題。
        dfsは再起的に設定すればいいが、
        bfsはどうするんだ？
        
        まずはroot nodeの値をres_listにappendする。

        次に、最初のself.leftと、self.rightに対して、操作する。
        valをcurr_listにappendする。
        average(curr_list)を、res_listにappendする

        ・・・ただこの方法だと、進めたポインタとTreeNodeを保持しておく必要があり、煩雑。
        dfs的に潜りながら、値を各階層に保持していく？
        コールスタックの深さに合わせて、appendするidxを選ぶとか。

        ただそれって、BFDじゃないよな・・・

        まずはroot nodeの値をres_listにappendする。
        次に、最初のself.leftと、self.rightに対して、操作する。
        valをcurr_listにappendする。
        TreeNodeインスタンスを、次の操作用に、list？に格納しておく？
        average(curr_list)を、res_listにappendする

        """
