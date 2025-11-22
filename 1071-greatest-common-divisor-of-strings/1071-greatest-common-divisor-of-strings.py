class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # If concatenation is not equal, no common divisor string
        if str1 + str2 != str2 + str1:
            return ""

        # Manual GCD function (Python 2 compatible)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        length = gcd(len(str1), len(str2))
        return str1[:length]
