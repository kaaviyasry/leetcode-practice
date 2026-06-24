class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum=0
        for i in range(len(s)):
            sum+=abs(i-t.index(s[i]))
        return sum
        