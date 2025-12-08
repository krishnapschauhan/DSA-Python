class Solution:
    def reverseSubArray(self, arr, l, r):
        # Convert 1-based index to 0-based index
        l -= 1
        r -= 1
        
        # Recursive function
        def helper(arr, i, j):
            if i >= j:
                return
            arr[i], arr[j] = arr[j], arr[i]
            helper(arr, i + 1, j - 1)

        helper(arr, l, r)
        return arr
