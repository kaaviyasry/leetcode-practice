class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        mul=1
        num=list(str(n))
        for i in range(len(num)):
            sum+=int(num[i])
            mul*=int(num[i])
        ans=sum+mul
        return n%ans==0

        