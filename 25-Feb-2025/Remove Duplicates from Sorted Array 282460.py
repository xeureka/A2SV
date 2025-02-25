# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        n = len(nums)

        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        

        return j
        



        