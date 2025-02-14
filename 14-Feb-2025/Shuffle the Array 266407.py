# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
            arr1 = nums[:n]
            arr2 = nums[n:]

            answer = []

            i,j = 0,0

            while i < n:
                answer.append(arr1[i])
                answer.append(arr2[j])
            
                i+= 1
                j += 1
            
            return answer

        