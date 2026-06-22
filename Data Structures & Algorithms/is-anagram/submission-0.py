class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1={}
        f2={}
        for i in s:
            if i in f1:
                f1[i]+=1
            else:
                f1[i]=1
        for j in t:
            if j in f2:
                f2[j]+=1
            else:
                f2[j]=1
        if f1 == f2:
            return True
        else:
            return False
        