class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            n1=list(str(n))
            mul=1
            for i in range(len(n1)):
                mul*=int(n1[i])
            if mul%t==0:
                return n
            else:
                n=n+1
        