class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        startでのminと、endでのマックスの幅が、全体での幅ではある。
        1つずつ含まれるか否かで、チェックしていけば、O(N)の空間計算量になる。
        もしくは、intervalひとつずつを処理して、
        次のインターバルが既存のインターバルと重複する場合、マージする、という方法
        こっちだと、インターバルの要素数の計算量になる。軽そう。
        [1,3], [2,6]→
        2つのインターバルを比較して、一方のend>=他方のstartだった場合、被っている。
        一方のstartが、他方のendよりも大きい場合、つまりith end<= i+1th start、
        (min(start, start), max(start, start))
        重複がない場合は、新しい区間として判定する。
        つまり、resultの区間を、別途保存しておく必要がありそう。
        このresult内の空間は、最後の項を判定するまでは、確定しない。
        
        """
