class Solution(object):
    def removeOuterParentheses(self, s):
        result = ""
        count = 0

        for ch in s:
            if ch == '(':
                if count > 0:
                    result += ch
                count += 1
            else:
                count -= 1
                if count > 0:
                    result += ch
        return result
        