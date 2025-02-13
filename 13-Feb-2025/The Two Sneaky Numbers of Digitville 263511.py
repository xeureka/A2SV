# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

            counter = {}
            ans = []

            for i in nums:
                if not i in counter:
                    counter[i] = 1
                
                else:
                    ans.append(i)
            
            return ans
        