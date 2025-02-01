# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        newS = s.split()

        hasmap = {}

        for word in newS:
            for i in word:
                if i.isnumeric():
                    hasmap[int(i)] = word.replace(i,'')
        
        new = OrderedDict(sorted(hasmap.items()))
        sent = new.values()
        
        answer = ''

        for i in sent:
            answer += i
            answer += ' '
        
        return answer.strip()
        