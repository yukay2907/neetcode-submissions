class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                word += i
        word = word.lower()
        if word == word[::-1]:
            return True
        return False