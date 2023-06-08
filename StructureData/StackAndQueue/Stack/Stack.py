from typing import Optional

from StructureData.StackAndQueue import Element


class Stack:
    def __init__(self):
        self.stack: Optional[Element] = None
        self._len: int = 0

    def __repr__(self):
        return (
            f'stack: {self.stack}'
            f'   lenght: {self._len}'
        )

    def __len__(self) -> int:
        return self._len

    def push(self, value):
        if self.stack:
            root = self.stack
            self.stack = Element(value)
            self.stack.previos = root
        else:
            self.stack = Element(value)
        self._len += 1

    def pop(self):
        if self._len > 0:
            value = self.stack.value
            self.stack = self.stack.previos
            self._len -= 1
            return value
        else:
            raise 'Stack is empty'

