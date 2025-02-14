# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
            good_pairs = 0
            counter = Counter(nums)

            for i,j in counter.items():
                good_pairs += j * (j - 1) // 2
            
            return good_pairs