class Solution:
    def replaceDigits(self, s: str) -> str:
        s=list(s)
        for i in range(1,len(s),2):
            x=int(s[i])
            s[i]=chr(ord(s[i-1])+x)
        return "".join(s)
        