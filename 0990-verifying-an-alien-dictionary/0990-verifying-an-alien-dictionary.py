class Solution:
    def isAlienSorted(self, words, order):
        order_map = {letter: i for i, letter in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order_map[c1] > order_map[c2]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True
