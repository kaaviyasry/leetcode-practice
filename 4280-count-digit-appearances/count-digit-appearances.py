class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count=0
        for i in nums:
            count+=str(i).count(str(digit))
            
        return count
        