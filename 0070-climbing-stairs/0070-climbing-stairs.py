class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1
