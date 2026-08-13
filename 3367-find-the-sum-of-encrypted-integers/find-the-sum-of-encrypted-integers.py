class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            num=str(nums[i])
            large=max(num)
            encrypt=int(large*len(num))
            sum+=encrypt
        return sum
        