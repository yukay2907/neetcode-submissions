class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r= len(s1)
        sorted_s1=''.join(sorted(s1))
        for i in range(len(s2)-r+1):
            word = s2[i:i+r]
            sorted_s2 =''.join(sorted(word))
            if sorted_s1 == sorted_s2:
                return True
        return False
