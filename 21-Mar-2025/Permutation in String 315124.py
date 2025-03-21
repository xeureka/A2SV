# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        b = len(s2)

        sorted_s1 = Counter(s1)

        n = b - a + 1

        for i in range(n):

            temp = Counter(s2[i:i+a])

            if temp == sorted_s1:
                return True
        
        return False


