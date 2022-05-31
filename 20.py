class Solution:
    def isValid(self, s: str) -> bool:
        opens = "([{"
        opposite = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if (c in opens):
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != opposite[c]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0