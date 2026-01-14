class Solution:
    def binarysearch(self, arr, k):
        low, high = 0, len(arr) - 1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                result = mid          # store answer
                high = mid - 1        # move left to find smaller index
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
                
        return result
