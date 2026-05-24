class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        list2=nums
        for i in nums:
            ans.append(i)
        for i in list2:
            ans.append(i)
        return ans

        
        