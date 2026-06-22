class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        nn = n
        if nn ==0:
            return 1
        if nn <0:
            nn *=-1
        while nn != 1:
            if nn%2:
                res = res*x
                nn = nn-1
            else:
                x = x*x
                nn = nn/2
        res = res * x
        if n <0:
            res = 1/res
        return res