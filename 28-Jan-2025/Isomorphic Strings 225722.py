# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:



        patter1,pattern2 = [],[]

        for i in s:
            patter1.append(s.index(i))
        
        for i in t:
            pattern2.append(t.index(i))
        
        return patter1 == pattern2

        
        