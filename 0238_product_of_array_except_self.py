class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        時間計算量がO(n)で、ということは、1重走査。
        先に全部のプロダクトを出してから、順に割り算する。
        のは禁止されているのか。division operationが使えないから。
        あー？スライディングウィンドウもだめか
        走査しながら、積を積み上げていく？
        """
