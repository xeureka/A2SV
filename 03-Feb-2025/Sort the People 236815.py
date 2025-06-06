# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):
        comb = list(zip(heights,names))
        comb.sort()

        answer = []

        for i in comb:
            answer.append(i[1])

        return answer[::-1]
        