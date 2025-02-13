# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        
        bucket = x
        rev_num = 0

        while x != 0:
            digit = x % 10
            rev_num = rev_num * 10 + digit
            x //= 10
        
        return bucket == rev_num