class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for i in range(1, len(strs[0])+1):
            prefix = strs[0][0:i]
            for word in strs:
                if not (word[0:i] == prefix):
                    return prefix[0:-1]
                
        return prefix