class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans1=[]
        ans2=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        for i in range(len(nums)):
            if nums[i]!=0:
                ans1.append(nums[i])
            else:
                ans2.append(nums[i])
        
        nums[:]=ans1+ans2
        return nums

        