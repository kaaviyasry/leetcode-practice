class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        ans = []

        for x in arr2:
            count = arr1.count(x)

            for i in range(count):
                ans.append(x)

            for i in range(count):
                arr1.remove(x)

        arr1.sort()

        return ans + arr1
        