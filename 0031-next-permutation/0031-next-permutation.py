class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        pivot = -1
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        
        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        nums[pivot+1:] = reversed(nums[pivot+1:])
