class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result = []
        for i in range(n):
            found = False
            for j in range (i,n):
                if temperatures[j]>temperatures[i]:
                    result.append(j-i)
                    found = True
                    break
            if not found:
                result.append(0)
        return result