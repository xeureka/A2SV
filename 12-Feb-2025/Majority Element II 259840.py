# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []

        for i,v in counter.items():
            if v > len(nums) // 3:
                ans.append(i)
        
        return ans