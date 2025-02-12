# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_lett = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        ans = 0
        
        for i in range(0, len(s)):
            
            if i < len(s) - 1 and roman_lett[s[i]] < roman_lett[s[i+1]]:
                
                ans -= roman_lett[s[i]]
                
    
            else:
                ans += roman_lett[s[i]]
                
        return ans

