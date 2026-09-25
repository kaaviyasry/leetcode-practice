class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff=[]
        for i in range(len(nums)):
            prefix=len(set(nums[:i+1]))
            sufix=len(set(nums[i+1:]))
            diff.append(prefix-sufix)
        return diff
        