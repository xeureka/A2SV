# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
            

        return len(nums)
        


        
        