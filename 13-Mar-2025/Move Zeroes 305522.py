# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0

        for index,value in enumerate(nums):
            if value != 0:
                nums[idx],nums[index] = nums[index],nums[idx]
                idx += 1
        


        