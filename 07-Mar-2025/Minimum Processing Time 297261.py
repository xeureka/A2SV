# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()

        tasks.sort()
        res = float("-inf")
        for i in range(0, len(tasks), 4):
            res = max(res, processorTime.pop() + max(tasks[i:i+4]))
        return res
        