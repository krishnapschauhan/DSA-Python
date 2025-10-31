class Solution:
    def maxProduct(self, nums):
        res = cur_max = cur_min = nums[0]
        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            res = max(res, cur_max)
        return res
