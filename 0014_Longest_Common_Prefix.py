class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        先頭の文字列が、全文字列で等しいパートを切り出す。
        文字列の最小長さをmとして、要素数をnとすると
        時間計算量は、O(m×n)
        空間計算量は、O(1)
        """
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in range(0, len(prefix)):
            for j in range(1, len(strs)):
                if i+1 > len(strs[j]):
                    return prefix[:i]
                if prefix[i] != strs[j][i]:
                    return prefix[:i]
        return prefix
