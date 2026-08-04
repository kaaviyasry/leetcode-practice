class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-1):
            start=nums[i]+1
            end=nums[i+1]
            while start<end:
                ans.append(start)
                start+=1
        return ans
        