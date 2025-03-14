# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
    # Bruteforce way

    # count = 0

    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] < target:
    #             count += 1
    
    # return count

    # '''
    #     Two Pointer for optimzation
    # '''
        nums.sort()

        i,j = 0,len(nums)-1
        count =0

        while i < j:
            if nums[i] + nums[j] < target:
                count += j - i
                i += 1
            
            else:
                j -= 1
        
        return count

        