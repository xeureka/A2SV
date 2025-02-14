# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            max_ones = 0
    
            ans = 0

            for i in nums:
                if i == 1:
                    ans += 1
                
                else:
                    max_ones = max(max_ones,ans)
                    ans = 0
            
            return max(max_ones,ans)
        