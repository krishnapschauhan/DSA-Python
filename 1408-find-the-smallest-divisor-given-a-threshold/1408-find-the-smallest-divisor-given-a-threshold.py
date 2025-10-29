class Solution(object):
    def smallestDivisor(self, nums, threshold):
        if threshold < len(nums):
            return -1
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            total = 0
            for num in nums:
                total += (num + mid - 1) // mid  
            if total <= threshold:
                high = mid
            else:
                low = mid + 1
        return low