class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones)>1:
            stones.sort()
            a=stones.pop()
            b=stones.pop()
            if a!=b:
                stones.append(a-b)
        if len(stones)==0:
            return 0
        return stones[0]
        