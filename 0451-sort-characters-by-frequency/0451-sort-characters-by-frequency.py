from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Count frequency of each character
        freq = Counter(s)

        # Step 2: Sort by frequency (highest first)
        sorted_chars = freq.most_common()

        # Step 3: Build result string
        result = ""
        for ch, count in sorted_chars:
            result += ch * count

        return result
