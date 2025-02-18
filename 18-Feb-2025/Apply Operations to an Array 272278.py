# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, arr: List[int]) -> List[int]:

        left,right = 0,1

        while right < len(arr):
            if arr[left] == arr[right]:
                arr[left],arr[right] = arr[left]*2,0
            
            left += 1
            right += 1
        
        idx = 0

        for index,value in enumerate(arr):
            if value != 0:
                arr[idx],arr[index] = arr[index],arr[idx]
                idx += 1
        
        return arr