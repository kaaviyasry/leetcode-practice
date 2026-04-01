class Solution(object):
    def minimumAverage(self, nums):

        nums.sort()
        n = len(nums)
        mini = float("inf")

        i = 0
        j = n - 1

        while i < j:
            avg = (nums[i] + nums[j]) / 2.0
            mini = min(mini, avg)
            i += 1
            j -= 1

        return mini
