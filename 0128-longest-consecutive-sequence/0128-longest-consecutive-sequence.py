class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        longest = 1
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:  
                current_num = num
                streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    streak += 1
                longest = max(longest, streak)
        return longest
