class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=list(str(n))
        prod=1
        sum=0
        for i in range(len(s)):
            sum+=int(s[i])
            prod*=int(s[i])
        ans=prod+sum
        return n%ans==0
        