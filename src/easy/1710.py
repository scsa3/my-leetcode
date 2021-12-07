from operator import itemgetter
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=itemgetter(1), reverse=True)
        result = 0
        for number, unit in boxTypes:
            if number <= truckSize:
                result += (number * unit)
                truckSize -= number
            else:
                result += (truckSize * unit)
                break
            if truckSize == 0:
                break
        return result