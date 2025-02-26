# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

            ans = []

            maxim = max(candies)

            for i in candies:
                if i+extraCandies >= maxim:
                    ans.append(True)
                else:
                    ans.append(False)
            

            return ans
        