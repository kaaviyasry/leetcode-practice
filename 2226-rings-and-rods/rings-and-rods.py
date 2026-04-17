class Solution:
    def countPoints(self, rings: str) -> int:
        count=0
        for i in range(10):
            i=str(i) #converting i into str
            if 'R'+i in rings and 'B'+i in rings and 'G'+i in rings:
                count+=1
        return count

        