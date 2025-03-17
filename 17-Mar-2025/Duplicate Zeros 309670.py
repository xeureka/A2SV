# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        new_arr = []

        for i in arr:
            if i != 0:
                new_arr.append(i)
            
            else:
                for _ in range(2):
                    new_arr.append(0)
        
        # return back the the original array

        for i in range(len(arr)):
            arr[i] = new_arr[i]
        
    


            
         
        
     
        