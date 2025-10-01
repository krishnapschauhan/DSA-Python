class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

obj = Solution()
print(obj.isPalindrome(121)) 
print(obj.isPalindrome(-121)) 
