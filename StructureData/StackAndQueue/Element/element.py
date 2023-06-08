from __future__ import annotations

from typing import Optional


class Element:
    def __init__(self, value):
        self._value = value
        self._next: Optional[Element] = None
        self._previos: Optional[Element] = None

    def __repr__(self):
        return f'element: {self._value}'

    @property
    def value(self):
        return self._value

    @property
    def previos(self):
        return self._previos

    @previos.setter
    def previos(self, value):
        self._previos = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value
