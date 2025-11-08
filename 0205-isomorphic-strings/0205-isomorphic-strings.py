class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        mapping_s_t = {}
        mapping_t_s = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in mapping_s_t and mapping_s_t[ch1] != ch2:
                return False
            if ch2 in mapping_t_s and mapping_t_s[ch2] != ch1:
                return False

            mapping_s_t[ch1] = ch2
            mapping_t_s[ch2] = ch1

        return True
