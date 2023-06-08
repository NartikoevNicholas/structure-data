from typing import Optional

from StructureData.StackAndQueue import Element


class MyQueue:
    def __init__(self):
        self._head: Optional[Element] = None
        self._tail: Optional[Element] = None
        self._len: int = 0

    def __len__(self):
        return self._len

    def __repr__(self):
        return (
            f'head: {self._head}'
            f'    tail: {self._tail}'
            f'    lenght: {self._len}'
        )

    def put(self, value):
        value = Element(value)
        if self._tail:
            tail = self._tail
            self._tail = value
            self._tail.previos = tail
            tail.next = self._tail
        else:
            self._head = value
            self._tail = value
        self._len += 1

    def get(self):
        if self._len > 0:
            value = self._head.value
            self._head = self._head.next
            if self._head:
                self._head.previos = None
            self._len -= 1
            return value
        else:
            raise 'Queue is empty'
