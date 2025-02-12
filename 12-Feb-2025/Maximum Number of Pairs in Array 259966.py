# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dd={}
        for i in nums:
            if i in dd:
                dd[i]+=1
            else:
                dd[i]=1
        count=0
        reme=0
        for i,j in dd.items():
            count+=j//2
            reme+=j%2
        return [count,reme]