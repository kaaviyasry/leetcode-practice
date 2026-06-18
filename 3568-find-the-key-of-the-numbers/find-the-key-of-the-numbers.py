class Solution(object):
    def generateKey(self, num1, num2, num3):
        num1 = str(num1).zfill(4)
        num2 = str(num2).zfill(4)
        num3 = str(num3).zfill(4)

        ans = ""

        for i in range(4):
            ans += min(num1[i], num2[i], num3[i])

        return int(ans)


        