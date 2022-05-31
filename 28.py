class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            good = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    good = False
                    break
            if good:
                return i
        
        return -1
                    