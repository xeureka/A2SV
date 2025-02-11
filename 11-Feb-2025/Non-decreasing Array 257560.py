# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, numbers: List[int]) -> bool:
        count = 0
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                count += 1


                if numbers[i-1] > numbers[i+1] and i != 0:
                    numbers[i+1] = numbers[i]


                elif numbers[i-1] < numbers[i+1] and i != 0:


                    numbers[i] = numbers[i+1]
        if count > 1:
            return True
        
        return False

