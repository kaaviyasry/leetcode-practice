class Solution(object):
    def moveZeroes(self, nums):
        j=0 #points to nxt idx
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
  
        