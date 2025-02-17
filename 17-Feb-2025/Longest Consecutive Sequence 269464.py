# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        hm = {}
        maximm = 0
        for num in nums:
            x = hm.get(num - 1, 0)
            y = hm.get(num + 1, 0)
            val = x + y + 1
            hm[num - x] = val
            hm[num + y] = val
            maximm = max(maximm, val)
        return maximm
