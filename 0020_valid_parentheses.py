class Solution:
    DIC = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    def isValid(self, s: str) -> bool:
        """
        stackの話。
        開いたものがつづいたら、最後に開いたかっこを閉じる。
        first in last out.        
        """
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if not s[i] in self.DIC:
                stack.append(s[i])
            if s[i] in self.DIC:
                if stack and stack.pop() == self.DIC[s[i]]:
                    continue
                else:
                    return False
        return not stack
