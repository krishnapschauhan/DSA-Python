class Solution(object):
    def subsets(self, nums):
        res = []
        
        def solve(ind, subset):
            if ind == len(nums):
                res.append(subset[:])
                return
            
           #Pick nums[ind]
            subset.append(nums[ind])
            solve(ind + 1, subset)
            
            #NOT pick nums[ind]
            subset.pop()
            solve(ind + 1, subset)

        solve(0, [])
        return res
