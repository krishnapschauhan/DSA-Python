class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        pos_index = 0
        neg_index = 1

        for x in nums:
            if x > 0:
                res[pos_index] = x
                pos_index += 2
            else:
                res[neg_index] = x
                neg_index += 2

        return res
