class Solution:
    
    def __init__(self):
        self.values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    
    def getValue(self, symbol: str) -> int:
        return self.values[symbol]
    
    def romanToInt(self, s: str) -> int:
        
        i = 0
        prevSymbol = s[i]
        currentValue = self.getValue(prevSymbol)
        totalValue = 0
        
        i += 1
        while i < len(s):
            currentSymbol = s[i]
            if self.getValue(currentSymbol) == self.getValue(prevSymbol):
                currentValue += self.getValue(currentSymbol)
            
            elif self.getValue(currentSymbol) < self.getValue(prevSymbol):
                totalValue += currentValue
                currentValue = self.getValue(currentSymbol)
                
            
            else:
                totalValue -= currentValue
                currentValue = self.getValue(currentSymbol)
                
            prevSymbol = s[i]
            i += 1
        
        totalValue += currentValue
        
        return totalValue
                
            
                
    
                