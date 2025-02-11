# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
  def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
    ghostSt = min(abs(x - target[0]) + abs(y - target[1]) for x, y in ghosts)

    return abs(target[0]) + abs(target[1]) < ghostSt