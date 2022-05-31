class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        
        i = 1
        while i < len(nums):
            if currentSum < 0:
                currentSum = nums[i]
                
            else:
                currentSum += nums[i]
                
            if currentSum > maxSum:
                maxSum = currentSum
            
            i += 1
        
        return maxSum
        