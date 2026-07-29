class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        sum=0
        sq=0
        num=list(str(n))
        for i in range(len(num)):
            sum+=int(num[i])
            sq+=pow(int(num[i]),2)
        return sq-sum>=50

        