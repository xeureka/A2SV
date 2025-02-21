# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

            matrix = []

            for im in image:
                matrix.append(im[::-1])
            
            answer = []

            for i in matrix:
                current = []

                for j in i:
                    if j == 1:
                        current.append(0)
                    else:
                        current.append(1)
                answer.append(current)
            
            return answer
        