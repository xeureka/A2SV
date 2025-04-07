# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
    
        temp = [0] * (n+1)
        
        for shift in shifts:
            start,end,d = shift
            
            if d == 1:
                temp[start] += 1
                temp[end+1] -= 1
            
            else:
                temp[start] -= 1
                temp[end+1] += 1
                
        
        for i in range(1,n):
            temp[i] += temp[i -1]
        
        
        result = [] 
        
        for i in range(n):
            # k = k % 26
            shift = temp[i] % 26
            
            position = (ord(s[i]) - ord('a') + shift) % 26 + ord('a')
            
            char =  chr(position)
            
            result.append(char)
        
        return ''.join(result)