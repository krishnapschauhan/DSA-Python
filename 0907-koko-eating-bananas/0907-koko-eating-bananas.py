class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            total_hrs = 0

            for p in piles:
                total_hrs += (p + mid - 1) // mid

            if total_hrs <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
