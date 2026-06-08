class Solution(object):
    def canAliceWin(self, nums):
        alice1=0
        bob1=0
        for i in nums: #case1
            if i>9:
                bob1+=i
            if i<10:
                alice1+=i
        alice2=0
        bob2=0
            
        for i in nums: #case 2
            if i<10:
                bob2+=i
            if i>9:
                alice2+=i
        if alice2>bob2 or alice1>bob1:
            return True
        else:
            return False
        

            
            
        