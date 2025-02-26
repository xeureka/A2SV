# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        pos = []
        neg = []

        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        
        final = []
        
        for i in range(len(pos)):
            final.append(pos[i])
            final.append(neg[i])
        
        return final
        