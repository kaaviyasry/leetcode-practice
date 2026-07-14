class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            ans=0
            n=list(str(num))
            for i in range(len(n)):
                ans+=int(n[i])  
            num=ans 
        return num

        
        