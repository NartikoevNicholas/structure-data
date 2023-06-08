class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None
        self.leftHeight: int = 0
        self.rightHeight: int = 0

    def __repr__(self):
        return (
            f'value = {self.value}'
            f'    left height =  {self.leftHeight}'
            f'    right height =  {self.rightHeight}'
            f'    parent =  {self.parent.value if self.parent else self.parent}'
        )

    def getMaxHeight(self):
        return self.leftHeight if self.leftHeight > self.rightHeight else self.rightHeight

    def resetHeight(self):
        self.rightHeight = self.right.getMaxHeight() + 1 if self.right else 0
        self.leftHeight = self.left.getMaxHeight() + 1 if self.left else 0

    def setLeft(self, value):
        self.left = value
        self.leftHeight = 0
        if value is not None:
            self.leftHeight = value.getMaxHeight() + 1
            value.parent = self

    def setRight(self, value):
        self.right = value
        self.rightHeight = 0
        if value is not None:
            self.rightHeight = value.getMaxHeight() + 1
            value.parent = self
