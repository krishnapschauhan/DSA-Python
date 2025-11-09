class Solution:
    def minTime(self, arr, k):
        if not arr or k <= 0:
            return -1
        if k > len(arr):
            return -1

        def isValid(arr, k, mid):
            painters = 1
            curr = 0
            for length in arr:
                if length > mid:
                    return False
                if curr + length <= mid:
                    curr += length
                else:
                    painters += 1
                    curr = length
                    if painters > k:
                        return False
            return True

        start = max(arr)
        end = sum(arr)
        ans = -1

        while start <= end:
            mid = (start + end) // 2
            if isValid(arr, k, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
