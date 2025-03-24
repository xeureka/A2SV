# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
            n = len(blocks)

            min_opr = float('inf')

            for i in range(n-k+1):
                w_count = 0

                for j in range(i,i+k):
                    if blocks[j] == 'W':
                        w_count += 1
                
                min_opr = min(min_opr,w_count)

            return min_opr