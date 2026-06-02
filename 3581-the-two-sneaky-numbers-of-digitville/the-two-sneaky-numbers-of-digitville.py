class Solution(object):
    def getSneakyNumbers(self, nums):
        ans=[]
        for i in nums:
            if nums.count(i)==2 and i not in ans:
                ans.append(i)
        return ans
        