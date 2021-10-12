from itertools import permutations
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = list()
        if turnedOn > 8:
            return []
        for h_wise in range(4):
            h_posible = set()
            m_posible = set()
            m_wise = turnedOn - h_wise
            if m_wise < 0:
                break

            h_bit_string = "1" * h_wise
            for s in permutations(h_bit_string.zfill(4), 4):
                h = int("".join(s), 2)
                if h < 12:
                    h_posible.add(h)

            m_bit_string = "1" * m_wise
            for s in permutations(m_bit_string.zfill(6), 6):
                m = int("".join(s), 2)
                if m < 60:
                    m_posible.add(m)

            for h in h_posible:
                for m in m_posible:
                    s = f"{h}:{m:02d}"
                    result.append(s)

        return result


if __name__ == '__main__':
    Solution().readBinaryWatch(1)
