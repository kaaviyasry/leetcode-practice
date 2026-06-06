class Solution(object):
    def maximumWealth(self, accounts):
        max=0
        for acc in accounts:
            sum=0
            for j in acc:
                sum+=j
                if(sum>max):
                     max=sum
                
        return max
                
        