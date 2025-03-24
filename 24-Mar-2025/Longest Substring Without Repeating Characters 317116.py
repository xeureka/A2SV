# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_subseq = []
        left,right = 0,0
        while right <= len(s) - 1:
            if s[right] not in current_subseq:
                current_subseq.append(s[right])
                right += 1
                max_length = max(max_length,len(current_subseq))
            else:
                current_subseq.remove(s[left])
                left += 1
        
        return max_length

                
   
        