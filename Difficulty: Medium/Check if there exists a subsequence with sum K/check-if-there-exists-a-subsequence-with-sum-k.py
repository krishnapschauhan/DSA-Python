class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        dp = [False] * (K + 1)
        dp[0] = True

        for num in arr:
            for s in range(K, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True

        return dp[K]
