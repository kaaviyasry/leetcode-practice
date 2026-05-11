class Solution(object):
    def removeOuterParentheses(self, s):
        count=0
        ans=""
        for ch in s:
            if count==0 and ch=='(':
                count=count+1
            elif  ch=='(':
                ans=ans+ch
                count=count+1
            elif count==1 and ch==')':
                count=count-1
            else:
                count=count-1
                ans=ans+ch 
        return ans