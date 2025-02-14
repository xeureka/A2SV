# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        one,two = 0,0
        word = []

        while one < len(word1) and two < len(word2):
            word.append(word1[one])
            word.append(word2[two])
            one += 1
            two += 1
        
        while one < len(word1):
            word.append(word1[one])
            one += 1
        
        while two < len(word2):
            word.append(word2[two])
            two += 1
        
        return ''.join(word)


        