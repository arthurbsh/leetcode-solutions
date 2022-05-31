class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = j = 0
        
        for _ in range(n):
            nums1.pop()
        
        while j < n:
            if i >= m + j or nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
            
            i += 1