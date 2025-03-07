# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, B: str) -> bool:
        return len(s) == len(B) and B in s*2
        