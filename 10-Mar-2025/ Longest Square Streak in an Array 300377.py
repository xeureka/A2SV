# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)

        count = -1

        for i in nums:

            temp = 0
        

            while i in s:
                temp += 1
                i *= i
            
            if temp > 1:
        
                count = max(count,temp)
        
        return count
            