class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        1日を代表する気温が配列に格納されている
        当日よりも高い気温が翌日以降にある場合、何日後か返す。
        heapに足していくか？
        73は、74をみて1を返して終了。
        74は、75をみて1を返して終了。
        75は、71をみてpass, 69pass, 72pass, 76をみて4を返して終了。
        各項目で後ろまで探しに行き続けるのはいけてない。
        未決定の項目はstackしておこう。
        73をスタックして（数値、インデックスを）、
        74に進んで、もしスタックが残っていたら、
        74と比較して、73＜74だから、1-0＝1を返して終了
        74もスタックする。
        75に進んで、おなじ。
        71に進んで、スタックに残っている75と比較して、何も起きない。
        71もスタックに追加する。
        お！スタックには降順で値が溜まっていく。
        69もスタックに追加する。
        72に進んで、
        スタックの69が69<72なのでresultが6-5＝1をappend、
        stack から69をpopして、
        スタックの71が71<72なのでresultが7-5＝2をappend、
        72をpopして、
        スタックの75は75＜72が不成立なので、スタックに溜まったまま。
        72をスタックに追加。
        """
        if not temperatures:
            return []

        res = {}
        stack = {} # num, idx
        for idx, num in enumerate(temperatures):
            # stackに要素がある場合
            if not stack:
                if stack[-1]
