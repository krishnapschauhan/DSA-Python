class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        total = m * k

        if total > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if self.canMake(bloomDay, m, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def canMake(self, bloomDay, m, k, days):
        bouquets = 0
        adjacent = 0

        for flower in bloomDay:
            if flower <= days:
                adjacent += 1
                if adjacent == k:
                    bouquets += 1
                    adjacent = 0
            else:
                adjacent = 0

        return bouquets >= m
