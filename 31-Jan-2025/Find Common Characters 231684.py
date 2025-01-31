# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
            answer = list(nums)

            for i in nums:
                answer.append(i)

            return answer
                