

class BinaryHeap:
    def __init__(self):
        self._values = []

    def __len__(self):
        return self._values.__len__()

    def add(self, value):
        self._values.append(value)
        self._siftUp(len(self._values) - 1)

    def extract(self):
        if self._values:
            root = self._values[0]
            self._swap(0, -1)
            del self._values[-1]
            self._siftDown(0)
            return root
        return None

    def getRoot(self):
        if self._values:
            return self._values[0]
        return None

    def heapify(self, array: list):
        self._values = array
        for i in range(len(array)):
            self._siftUp(i)

    def heapSort(self) -> list:
        result = []
        while self._values.__len__() > 0:
            result.append(self.extract())
        return result

    def _siftUp(self, i: int):
        ...

    def _siftDown(self, i: int):
        ...

    def _swap(self, i: int, j: int):
        value = self._values[i]
        self._values[i] = self._values[j]
        self._values[j] = value

    def _swapAndReturn(self, i, j):
        self._swap(i, j)
        return j

    @staticmethod
    def _parentIndex(i: int) -> int:
        return int((i - 1) / 2)

    @staticmethod
    def _leftChildIndex(i):
        return (2 * i) + 1

    @staticmethod
    def _rightChildIndex(i):
        return (2 * i) + 2
