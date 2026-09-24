class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
       
        for i in range(len(nums)):
            nums=list(nums)
            sum=0
            for j in str(nums[i]):
                sum+=int(j)
            if i==sum:
                return i
        return -1
        