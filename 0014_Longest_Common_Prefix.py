class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for other_word in strs[1:]:
                # インデックスが他の単語の長さを超えている、または文字が一致しない場合
                if i >= len(other_word) or other_word[i] != char:
                    return strs[0][:i]
                    
        # すべて一致してループを抜け切った場合
        return strs[0]
