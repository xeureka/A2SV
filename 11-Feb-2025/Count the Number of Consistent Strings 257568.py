# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
            count = 0
    
            for i in words:
                cons = True
                
                for char in i:
                    if char not in allowed:
                        cons = False
                        break
                        
                if cons:
                    count += 1
                    
            return count
        