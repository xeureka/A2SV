# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
            left,right = 0,0
            players.sort()
            trainers.sort()
    
            cnt = 0

            while left < len(players) and right < len(trainers):

                if players[left] <= trainers[right]:
                    cnt += 1
                    left += 1
                    right += 1
                
                else:
                    right += 1
            
            return cnt
        