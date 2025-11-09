class Solution(object):
    def splitArray(self, nums, k):
        if not nums or k <= 0:
            return -1
        if k > len(nums):
            return -1

        def isValid(nums, k, mid):
            subarrays = 1
            curr_sum = 0
            for num in nums:
                if num > mid:
                    return False
                if curr_sum + num <= mid:
                    curr_sum += num
                else:
                    subarrays += 1
                    curr_sum = num
                    if subarrays > k:
                        return False
            return True

        start = max(nums)
        end = sum(nums)
        ans = -1

        while start <= end:
            mid = (start + end) // 2
            if isValid(nums, k, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
