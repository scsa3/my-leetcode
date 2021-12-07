from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        times = set()
        for t in timeSeries:
            for i in range(t, t + duration):
                times.add(i)
        return len(times)