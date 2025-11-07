class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]
