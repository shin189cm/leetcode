class Solution:
    def trap(self, height: list[int]) -> int:
        """
        前回は、局所最適化を行って失敗した。
        幅1で水量を考えていく方針はイメージできていたのと、
        左右のポインタを狭めていく思想はできていた。
        ▼方針
        左のmaxと右のmaxを比較する。
        小さいほうを動かす。
        今のheightt[idx]と高さを比較する。
        その差だけ、水が貯まる。として足し上げる。
        これをleftとrightが等しくなるまで続ける。

        constraint
        height.lengthは1以上だから、ベースケースの処理は不要。
        """
        left, right = 0, len(height)-1
        res_water = 0
        max_left, max_right = 0, 0

        while left < right:
            # もしleftのほうが値が小さい場合、leftが律速なので、leftを動かす。
            if height[left] < height[right]:
                res_water += max(0, max_left - height[left])
                # max_leftを更新する
                max_left = max(max_left, height[left])
                # ポインタ更新
                left += 1
            else:
                res_water += max(0, max_right - height[right])
                # max_rightを更新
                max_right = max(max_right, height[right])
                # ポインタ更新
                right -= 1
                
        return res_water
