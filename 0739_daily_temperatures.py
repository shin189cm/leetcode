class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        何日後に、今日よりも暑い日が来るか。
        温度は配列から取得できるので、保存しておくのはINDEXのみでよい。
        配列は10^5のため、2重ループすると、10^10でTLEになる。

        次のより暖かい日が来るまで、スタックしておく。
        """
        # ベースケース。インデックスエラーを裁く。
        if not temperatures:
            return []

        # 変数宣言
        # idxだけ保持しておく。
        idx = [0] * len(temperatures)
        stack = [temperatures[0]]

        # 処理
        for i in range(1, len(temperatures)):
            if temperatures[i] > temperatures[i-1]:
                
