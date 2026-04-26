from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter(nums) #counting frequency
        for i in count.values():
            if i%2!=0:
                return False
        return True
        