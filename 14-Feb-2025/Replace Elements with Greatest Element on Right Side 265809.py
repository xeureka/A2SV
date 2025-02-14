# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_one = -1
        result = []

        for i in range(len(arr) -1,-1,-1):
            result.append(max_one)
            max_one = max(max_one,arr[i])
        
        return result[::-1]
            