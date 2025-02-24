# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:

            ans = ''
    

            for i in address:
                if i == '.':
                    ans = ans + '[.]'
                
                else:
                    ans += i
            return ans
        