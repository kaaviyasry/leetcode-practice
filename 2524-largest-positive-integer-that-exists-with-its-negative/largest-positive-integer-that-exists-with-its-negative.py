class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxi=-1
        for i in range(len(nums)):
            if -nums[i] in nums:
                maxi=max(maxi,abs(nums[i]))

        return maxi
        