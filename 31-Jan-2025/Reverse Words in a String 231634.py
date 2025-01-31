# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst.reverse()
        
        ans = ''

        for i in lst:
            ans += ' '
            ans += i

        return ans.strip()
        