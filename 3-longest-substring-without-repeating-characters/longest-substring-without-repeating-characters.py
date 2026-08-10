class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=[]
        maxi=0
        for i in range(len(s)):
            if s[i] not in ans:
                ans.append(s[i])
            else:
                ans=ans[ans.index(s[i])+1:]
                ans.append(s[i])
            maxi=max(maxi,len(ans))
        return maxi
        