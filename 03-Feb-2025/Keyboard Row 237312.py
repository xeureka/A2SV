# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = 'qwertyuiop'
        second = 'asdfghjkl'
        third = 'zxcvbnm'


        if len(words) == 2:
            return words

        di = defaultdict(list)

        for word in words:


            if all(char.lower() in first for char in word):
                di['answer'].append(word)
            
            elif all(char.lower()  in second for char in word):
                di['answer'].append(word)
            
            elif all(char.lower()  in third for char in word):
                di['answer'].append(word)
            
        final = di.values()

        if final:
            for i in final:
                return i
        else:
            return []

        