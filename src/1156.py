from typing import List


class OrderedStream:
    stream: list
    ptr: int

    def __init__(self, n: int):
        self.stream = [0] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        i = idKey - 1
        self.stream[i] = value
        result = []
        temp = self.ptr
        for index in range(self.ptr, len(self.stream)):
            if self.stream[index]:
                result.append(self.stream[index])
                temp = index + 1
            else:
                break
        self.ptr = temp
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)