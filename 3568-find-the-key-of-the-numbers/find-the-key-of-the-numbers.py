class Solution(object):
    def generateKey(self, num1, num2, num3):
        n1=str(num1).zfill(4)
        n2=str(num2).zfill(4)
        n3=str(num3).zfill(4)
        ans=""
        for i in range(4):
            ans+=min(n1[i],n2[i],n3[i])
        return int(ans)


        