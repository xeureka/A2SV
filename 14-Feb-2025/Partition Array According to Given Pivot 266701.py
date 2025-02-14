# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
            less = []
            up = []
            equal = []

            for i in nums:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    up.append(i)
                else:
                    equal.append(i)
            
            final = []
            for i in less:
                final.append(i)
            
            for i in equal:
                final.append(i)
            
            for i in up:
                final.append(i)

            return final