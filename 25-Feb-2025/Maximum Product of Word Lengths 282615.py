# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
            ans = 0

            for i in range(len(words) - 1) :
                for j in range(i,len(words)):
                    if set(words[i]) & set(words[j]) == set():

                        prod = len(words[i]) * len(words[j])

                        ans = max(prod,ans)
            
            return ans
                