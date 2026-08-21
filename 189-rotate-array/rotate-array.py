class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        ans1=[]
        ans2=[]
        n=len(nums)
        k=k%n
        for i in range(n):
            if i>=n-k:
                ans1.append(nums[i])
            else:
                ans2.append(nums[i])
        nums[:]=ans1+ans2
        