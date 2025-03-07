# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        count = 0

        for i in range(n -1,0,-1):
            if nums[i] != nums[i-1]:
                count += n - i
        
        return count