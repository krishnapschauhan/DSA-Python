class Solution(object):
    def singleNonDuplicate(self, nums):
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid
        
        return nums[start]
