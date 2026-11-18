"""
模擬試験
"""
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if not prerequisites:
            return True # イニシャルはキャピタル

        from_to = [[] for _ in range(numCourses)] # 0-indexed, これを受けると事前受講要件を1つ満たす先のコース
        course_num_pre = [0] * numCourses # 必要な事前履修数の残り
        for item in prerequisites:
            from_to[item[1]].append(item[0])
            course_num_pre[item[0]] += 1 # item[0]は、事前にitem[1]を履修する必要がある

        queue :deque[int] = deque([])
        for idx, item in enumerate(course_num_pre):
            if item == 0:
                queue.append(idx)

        while queue:
            curr_len = len(queue) # 意味ないかも
            for i in range(curr_len):
                curr_course = queue.popleft() # 履修した！
                numCourses -= 1
                for item in from_to[curr_course]:
                    course_num_pre[item] -= 1 # 事前準備が必要なコース数を1減らす
                    if course_num_pre[item] == 0:
                        queue.append(item)
        return True if numCourses == 0 else False
