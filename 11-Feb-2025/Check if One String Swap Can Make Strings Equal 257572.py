# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
  def areAlmostEqual(self, s1: str, s2: str) -> bool:
    dif = [i for i, (a, b) in enumerate(zip(s1, s2))
                   if a != b]
    return not dif or (len(dif) == 2 and s1[dif[0]] == s2[dif[1]] and s1[dif[1]] == s2[dif[0]])