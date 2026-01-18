class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        
        # Length mismatch → impossible
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for ch, word in zip(pattern, words):
            # If mapping already exists, it must match
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word
            
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch
        
        return True
