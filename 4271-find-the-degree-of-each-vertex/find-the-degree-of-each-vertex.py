class Solution(object):
    def findDegrees(self, matrix):
        ans=[]
        for i in matrix:
            sum=0
            for j in i:
                if j>=0:
                    sum+=j
            ans.append(sum)
        return ans
            

        