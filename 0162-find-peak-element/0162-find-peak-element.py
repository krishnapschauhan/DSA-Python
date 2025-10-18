class Solution(object):
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
                
        return start
