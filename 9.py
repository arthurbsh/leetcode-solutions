class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        
        x_str_inv = x_str[::-1] #
        
        print(x_str)
        print(x_str_inv)
        
        return x_str == x_str_inv