class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        maxi = 0
        word = ""

        while r < len(s):
            if s[r] not in word:
                word += s[r]
            else:
                word += s[r]
                if s[r] == s[l]:
                    l += 1
                else:
                    l = r
                word = word[l:]
            r += 1
            maxi = max(maxi,len(word))
        return maxi