class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        2pointers。
        狭めていく。
        水は低い壁に依存する。
        """
        # ベースケース
        if len(height) == 0:
            return 0
        
        # 変数設定
        left_point, right_point = 0, len(height) - 1
        max_water = 0

        while left_point < right_point:
            # 現在の水量
            current_water = min(height[right_point],height[left_point]) * (right_point - left_point)
            # 比較してリプレイス
            if max_water < current_water:
                max_water = current_water

            # ポインタを動かす。小さい方を動かす。
            if height[left_point] < height[right_point]:
                left_point += 1
            else:
                right_point -= 1
        
        return max_water
