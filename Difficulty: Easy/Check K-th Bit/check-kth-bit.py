class Solution:
    def checkKthBit(self, n, k):
        if((n>>k)&1)==1:
            return True
        else:
            return False
        