class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n1=list(str(n))
        sum=0
        mul=1
        for i in range(len(n1)):
            sum+=int(n1[i])
            mul*=int(n1[i])
        return mul-sum
        