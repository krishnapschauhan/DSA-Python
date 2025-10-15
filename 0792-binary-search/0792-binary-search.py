class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) / 2

            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1

        return -1
