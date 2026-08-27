class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            word = strs[i]
            sortedWord = ''.join(sorted(word))
            hashmap[sortedWord].append(word)
        res = []
        for _,value in hashmap.items():
            res.append(value)
        return res