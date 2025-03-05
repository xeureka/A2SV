# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        you = 0
        
        i = 1
        for _ in range(len(piles) // 3):
            you += piles[i]
            i += 2
        
        return you