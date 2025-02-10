# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            soorted_s = "".join(sorted(s))

            anagrams[soorted_s].append(s)
        
        return list(anagrams.values())