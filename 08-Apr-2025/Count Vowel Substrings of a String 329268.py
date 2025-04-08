# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
            vowel = set('aeiou')

            count = 0

            for i in range(len(word)):

                if word[i] not in vowel:
                    continue

                t = set()
                for j in range(i,len(word)):
                    if word[j] not in vowel:
                        break

                    t.add(word[j])

                    if len(t) == 5:
                        count += 1
            
            return count
