# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        tracked = set()

        while n != 1 and (not n in tracked):
            tracked.add(n)

            n = sum(int(i) ** 2 for i in str(n))
            
        return n==1