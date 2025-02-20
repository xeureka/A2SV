# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        lst = [num for num in range(1, n + 1)]

        idx = 0 

        while len(lst) > 1:

            elected_ones = (idx + (k-1)) % len(lst)

            lst.pop(elected_ones)

            idx = elected_ones

        return lst[0]