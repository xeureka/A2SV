# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dd = defaultdict(int)

        for i in nums:
            dd[i] += 1
        

        n =len(nums) // 2

        for key,value in dd.items():
            if value > n:
                return key