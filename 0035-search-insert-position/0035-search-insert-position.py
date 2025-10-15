class Solution(object):
    def searchInsert(self, nums, target):
        start=0
        end=len(nums)-1
        ans=len(nums)
        while start<=end:
            middle=(start+end)//2

            if nums[middle] >= target:
                ans=middle
                end=middle-1

            else:
                start=middle+1

        return ans
        