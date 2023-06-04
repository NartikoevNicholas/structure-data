from .BinaryHeap import BinaryHeap


class BinaryHeapMin(BinaryHeap):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'heap min: {self._values}'

    def _siftUp(self, i: int):
        while i > 0 and self._values[i] < self._values[self._parentIndex(i)]:
            parent_index = self._parentIndex(i)
            i = self._swapAndReturn(i, parent_index)

    def _siftDown(self, i: int):
        while (2 * i) + 2 < self.__len__():
            left_index = self._leftChildIndex(i)
            right_index = self._rightChildIndex(i)

            left = self._values[left_index]
            right = self._values[right_index]
            if self._values[i] <= left and self._values[i] <= right:
                break

            if left - right >= 0:
                i = self._swapAndReturn(i, right_index)
            else:
                i = self._swapAndReturn(i, left_index)

        if (2 * i) + 1 < self.__len__() and self._values[i] > self._values[(2 * i) + 1]:
            self._swap(i, (2 * i) + 1)
