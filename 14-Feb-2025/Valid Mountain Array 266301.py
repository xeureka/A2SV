# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
            if len(arr) < 3 or arr[0] > arr[1]:
                return False
            
            increasing = True

            for left,right in zip(arr,arr[1:]):
                if left == right:
                    return False
                
                if left < right and not increasing:

                    return False
                
                if left > right:
                    increasing = False
            
            return not increasing

        