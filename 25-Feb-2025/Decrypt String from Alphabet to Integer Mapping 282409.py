# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        lower = list(string.ascii_lowercase)

        res = []
        idx = len(s) - 1
        while idx >= 0:
            if s[idx] == "#":
                i = s[idx-2:idx]
                idx -= 2
            else:
                i = s[idx]
            res.append(lower[int(i)-1])
            idx -= 1

        return "".join(res)[::-1]