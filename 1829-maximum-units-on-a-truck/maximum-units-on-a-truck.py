class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total=0
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        for i in boxTypes:
            box=i[0]
            unit=i[1]
            if box<=truckSize:
                total+=box*unit
                truckSize-=box
            else:
                total+=truckSize*unit
                break
        return total
        