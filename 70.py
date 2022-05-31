class Solution:
    
    def __init__(self):
        self.results = {}
        
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        
        if n-2 not in self.results.keys():
            self.results[n-2] = self.climbStairs(n-2)
        
        if n-1 not in self.results.keys():
            self.results[n-1] = self.climbStairs(n-1)
        
        return self.results[n-1] + self.results[n-2]