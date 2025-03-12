# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        idx = 0

        for i,gr in enumerate(g):
            
            while idx < len(s) and s[idx] < gr:
                idx += 1
            
            if idx >= len(s):
                return i
            
            idx += 1
        
        return len(g)
            