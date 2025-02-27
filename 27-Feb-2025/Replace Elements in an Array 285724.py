# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        numToindex = {num:i for i,num in enumerate(nums)}

        for original,replaced  in operations:
            idx = numToindex[original]

            nums[idx] = replaced

            del numToindex[original]
            numToindex[replaced] = idx
        
        return nums