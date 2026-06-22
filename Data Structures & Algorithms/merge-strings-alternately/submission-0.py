class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1),len(word2))
        word3= ''
        for i in range(l):
            word3 += word1[i]
            word3 += word2[i]
        if len(word1)>len(word2):
            for i in range(l,len(word1)):
                word3 += word1[i]
        else:
            for i in range(l,len(word2)):
                word3 += word2[i]
        return word3