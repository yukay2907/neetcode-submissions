class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        s = ""
        for i in strs:
            ans += i
            s = s + i + "-"
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        ans = ""
        for i in range(len(s)):
            if s[i] != "-":
                ans = ans + s[i]
            else:
                result.append(ans)
                ans = ""
        return result