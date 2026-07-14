class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum1=0
        sum2=0
        num=list(str(n))
        for i in range(len(num)):
            if i%2==0:
                sum1+=int(num[i])
            else:
                sum2-=int(num[i])
        return sum1+sum2
        