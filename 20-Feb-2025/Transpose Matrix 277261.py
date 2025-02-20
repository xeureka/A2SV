# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []

        for i in range(len(matrix[0])):

            new_row = []

            for j in range(len(matrix)):
                new_row.append(matrix[j][i])

            transpose.append(new_row)
        
        return transpose