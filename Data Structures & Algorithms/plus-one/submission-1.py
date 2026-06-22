class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=len(digits)
        for i in range(x-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1] + digits