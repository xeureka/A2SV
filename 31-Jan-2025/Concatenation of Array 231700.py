# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            answer = list(nums)

            for i in nums:
                answer.append(i)

            return answer
                