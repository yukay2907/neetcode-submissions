class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + s + "~"
        return result
    def decode(self, s: str) -> List[str]:
        result=""
        res=[]
        for char in s:
            if char!= "~":
                result +=char
            else:
                res.append(result)
                result=""
        return res