from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag=defaultdict(list)
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            anag[sorted_s].append(s)
        for val in anag.values():
            result.append(val)
        return result