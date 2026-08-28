class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        i = 0
        maxLength = 0

        for j in range(len(s)):
            if s[j] in hashmap:
                i = max(i, hashmap[s[j]] + 1)

            hashmap[s[j]] = j
            maxLength = max(maxLength, j - i + 1)

        return maxLength