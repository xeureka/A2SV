# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []

        for i,v in counter.items():
            if v >= 2:
                ans.append(i)


        return ans
            