from typing import*
from collections import defaultdict
from string import ascii_lowercase

class Solution(object):
    def clearStars(self, s):
        char_idx = defaultdict(list)
        n = len(s)

        remove = [False]*n

        for i,char in enumerate(s):
            if char == '*':
                remove[i] = True

                for alpha in ascii_lowercase:
                    if char_idx[alpha]:
                        remove[char_idx[alpha].pop()] = True
                        break
            else:
                char_idx[char].append(i)
        
        return ''.join(char for i,char in enumerate(s) if not remove[i])
        