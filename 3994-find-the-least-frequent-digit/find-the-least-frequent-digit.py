class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=list(str(n))
        cot=[]
        for i in range(len(s)):
            cot.append([s.count(s[i]),int(s[i])])
        cot.sort()
        return cot[0][1]

        