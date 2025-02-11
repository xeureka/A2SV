# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []

        def sum_even(lst:list):
            sum = 0

            for i in lst:
                if i % 2 == 0:
                    sum += i
            
            return sum
        evenS = sum_even(nums)
        


        for item in queries:

            idx = item[1]
            prev = nums[idx]

            nums[idx] = nums[idx] + item[0]

            if nums[idx] % 2 == 0:
                evenS += nums[idx] - prev
            else:
                evenS -= prev

            ans.append(evenS + 1)

        
        
        return ans
        