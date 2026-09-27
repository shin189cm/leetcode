class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        履修。
        条件、aをうけるには、bをまず受けてください。
        解き方
        （1）事前履修が不要なコースを受講。完了コース数を足し上げ。
        （2）完了コースを必要コースから取り除く
        （3）事前履修が完了したコースを受講。完了コースを足し上げ。
        （4）履修済みコース数が、全体コース数と一致するか判定
        """
        # 各コースで事前履修が必要な履修コース数
        num_prepare = [0] * len(numCourses)
        for i in prerequisites:
            num_prepare[i[0]] += 1
        
        # 準備が0のコースを条件で抽出する
        ready_course = num

        # 
