# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        answer = ['']*len(s)
        i = 0

        for j in s:
            answer[indices[i]] = j
            i += 1
        
        return ''.join(answer)
        