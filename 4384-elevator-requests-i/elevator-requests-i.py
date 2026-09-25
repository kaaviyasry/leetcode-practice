class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total=0
        current=0
        for r in requests:
            total+=abs(current-r)
            current=r
        return total
        