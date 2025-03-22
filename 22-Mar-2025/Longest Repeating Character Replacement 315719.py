# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        max_len = 0
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            while r - l + 1 - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len 