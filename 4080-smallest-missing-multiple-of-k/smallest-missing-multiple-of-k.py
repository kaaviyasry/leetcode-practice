class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in range(len(nums)):
            if nums[i]%k==0:
                ans.append(nums[i])
        if len(ans)==0:
            return k
        for i in range(k,max(ans)+2*k,k):
            if i not in ans:
                return i
        