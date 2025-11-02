class Solution(object):
    def reverseWords(self, s):
          # Split the string into words (automatically removes extra spaces)
        words = s.split()
        
        # Reverse the list of words and join with a single space
        return ' '.join(reversed(words))
        