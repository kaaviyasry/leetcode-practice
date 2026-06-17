class Solution(object):
    def averageValue(self, nums):
        sum=0
        count=0
        for i in range(len(nums)):
            if nums[i]%3==0 and nums[i]%2==0:
                count+=1
                sum+=nums[i]
        if count==0:
            return count

        return sum//count
        