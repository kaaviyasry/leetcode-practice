class Solution(object):
    def moveZeroes(self, nums):
        ans1=[]
        ans2=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                ans1.append(nums[i])
            else:
                ans2.append(nums[i])
        nums[:]=ans1+ans2
        
  
        