# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:


        current_sum = sum([i for i in nums if i % 2 == 0])

        ans = []

        for query in queries:

            val,idx = query

            if nums[idx] % 2 == 0:

                current_sum -= nums[idx]
            
            nums[idx] += val

            if nums[idx] % 2 == 0:
                current_sum += nums[idx]
            
            ans.append(current_sum)

        return ans
       