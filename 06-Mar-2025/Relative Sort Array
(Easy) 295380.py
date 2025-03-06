# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/



class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {num: idx for idx, num in enumerate(arr2)}

        def sort_key(num):

            return (count.get(num, float('inf')), num)

        return sorted(arr1, key=sort_key)

