class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while right - left > 2:
            middle = int ( (left + right) / 2)
            
            if target > nums[middle]:
                left = middle
            else:
                right = middle
                
        for i in range(left, right + 1):
            if target <= nums[i]:
                return i
        
        return right + 1
        