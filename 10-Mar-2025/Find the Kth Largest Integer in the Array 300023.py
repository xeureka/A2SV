# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
            new_num = sorted([int(i) for i in nums],reverse=True)

            return str(new_num[k-1])
        