class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        list=[]
        a=0
        maxcandy=max(candies)
        for i in range(len(candies)):
            a=candies[i]+extraCandies
            if a>=maxcandy:
                list.append(True)
            else:
                list.append(False)
        return list

        