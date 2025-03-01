# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

            larg_one = [0,0]

            for idx,ma in enumerate(mat):
                
                if larg_one[1] < ma.count(1):
                    larg_one[0],larg_one[1] = idx,ma.count(1)


            return larg_one
        