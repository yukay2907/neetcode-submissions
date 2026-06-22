class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        result = []
        for num in digits:
            number += str(num)
        number = int(number) + 1
        for num in str(number):
            result.append(int(num))
        return result