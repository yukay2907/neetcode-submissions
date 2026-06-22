class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        res = []
        for word in strs:
            k = "".join(sorted(word))
            ana[k].append(word)
        for i in ana:
            res.append(ana[i])
        return res