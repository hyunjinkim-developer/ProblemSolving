class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key=len)
        min_len = len(min_str)
        
        common_prefix = ""
        for i in range(min_len + 1):
            for word in strs:
                if word == "":
                    continue
                if min_str[:i+1] != word[:i+1]:
                    return common_prefix
            common_prefix = min_str[:i+1]
        return common_prefix
