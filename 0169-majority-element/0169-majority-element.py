class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            
        majority=max(freq,key=freq.get)
        return majority
        