class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        for i in range(n):
            a.append(nums[i])  #prints x1 then go to nxt step and print y1
            a.append(nums[i+n])
        return a
        