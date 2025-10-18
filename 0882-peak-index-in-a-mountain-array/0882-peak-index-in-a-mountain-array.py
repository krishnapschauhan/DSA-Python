class Solution(object):
    def peakIndexInMountainArray(self, nums):
        start = 1
        end = len(nums) - 2

        while start <= end:
            mid = (start + end) // 2

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        return -1 
