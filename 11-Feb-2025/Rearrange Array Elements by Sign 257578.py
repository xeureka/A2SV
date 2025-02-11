# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        postive = [i for i in nums if i > 0]
        negative = [i for i in nums if i < 0]
        l = len(nums)
        lst = [0]*l
        j = 0
        k = 0
        for i in range(l):
            if i % 2 == 0:
                lst[i] = postive[j]
                j+=1
            else:
                lst[i] = negative[k]
                k+=1
        return lst