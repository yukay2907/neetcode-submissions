class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n
        while number != 0:
            number = sum(int(digit) ** 2 for digit in str(number))
            print(number)
            if number == 1:
                return True
            if number in seen:
                return False
            seen.add(number)