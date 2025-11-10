class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        if len(s)==len(t):
            if sorted(s)==sorted(t):
                return True
        return False
        