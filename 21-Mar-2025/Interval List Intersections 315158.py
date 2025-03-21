# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
            
        result = []

        i,j = 0,0

        while i < len(firstList) and j < len(secondList):

            # max of start and min of end

            start = max(firstList[i][0],secondList[j][0])
            end = min(firstList[i][1],secondList[j][1])

            if start <= end:

                result.append([start,end])
            

            if firstList[i][1] < secondList[j][1]:
                i += 1
            
            else:
                j += 1
        
        return result