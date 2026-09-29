class Solution:
    def minimumChairs(self, s: str) -> int:
        ans=0
        count=0
        for i in s:
            if i=='E':
                count+=1
                ans=max(ans,count)
            elif i=='L':
                count-=1
        return ans

        