class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for char in s:
            count[ord('a') - ord(char)] +=1
        for char in t:
            count[ord('a') - ord(char)] -=1
        
        for num in count:
            if num != 0:
                return False
        return True