class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        sum=0
        for idx,i in enumerate(nums):
            if idx%2==0:
                sum+=i
            else:
                sum-=i
        return sum