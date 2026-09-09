class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        sum1=0
        sum2=0
        mul=1
        for i in range(len(nums)):
            sum1=nums[0]*nums[1]
            sum2=nums[-1]*nums[-2]
            mul=abs(sum1-sum2)
        return mul