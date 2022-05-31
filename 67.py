class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        lenA = len(a)
        lenB = len(b)
        
        #make strings same length
        if lenA < lenB:
            a = '0'* (lenB - lenA) + a
        elif lenB < lenA:
            b = '0'* (lenA - lenB) + b
        
        carry = 0
        
        result = ""
        currentSum = 0
        
        i = 0
        
        while i < len(a):
            currentSum = int (a[-1 - i]) + int(b[-1 -i]) + carry
            
            #add bit
            result = str(currentSum % 2) + result
            
            carry = 1 if currentSum > 1 else 0
            
            i += 1
            
        
        if carry > 0:
            result = str(carry) + result
            
        return result