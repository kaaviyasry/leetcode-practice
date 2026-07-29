class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for i in range(len(arr)):
            if arr.count(arr[i]) == arr[i]:
                ans = max(ans, arr[i])
        return ans
        