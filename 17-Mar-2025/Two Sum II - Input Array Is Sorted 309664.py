# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = [0]*2

        left,right = 0,len(numbers)-1

        while left < right:

            summ = numbers[left] + numbers[right]

            if  summ == target:
                ans[0],ans[1] = left+1,right+1
                return ans

            elif summ > target:
                right -= 1
            
            else:
                left += 1
        