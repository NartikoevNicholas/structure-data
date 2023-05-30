from Node import Node


class AVLTree:
    def __init__(self):
        self.root = None
        self._len = 0

    def __repr__(self):
        return (
            f'tree:  [ {self.root} ];'
            f'    length:  {self._len};'
        )

    def __len__(self):
        return self._len

    def max(self):
        if self.root:
            result = self.root
            while True:
                if result.right is None:
                    return result.value
                result = result.right
        return None

    def min(self):
        if self.root:
            result = self.root
            while True:
                if result.left is None:
                    return result.value
                result = result.left
        return None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            self._len += 1
        else:
            self._add(self.root, value)

    def _add(self, node: Node, value):
        if node.value > value:
            if node.left is None:
                node.setLeft(Node(value))
                self._len += 1
                self._rotate(node)
            else:
                self._add(node.left, value)

        elif node.value <= value:
            if node.right is None:
                node.setRight(Node(value))
                self._len += 1
                self._rotate(node)
            else:
                self._add(node.right, value)

    def remove(self, value):
        if self.root:
            self._remove(self.root, value)

    def _remove(self, node: Node | None, value):
        if node:
            if node.value == value:
                self._len -= 1
                # когда есть и правый и левый ребенок
                if node.left and node.right:
                    if node.left.right is None:
                        node.value = node.left.value
                        node.setLeft(node.left.left)
                        self._rotate(node, False)
                        pass
                    else:
                        result = node.left
                        while True:
                            if result.right is None:
                                new_value = result.value
                                start = result.parent
                                result.parent.setRight(result.left)
                                break
                            result = result.right
                        node.value = new_value
                        self._rotate(start, False)
                        pass

                # когда есть только левый ребенок
                elif node.left:
                    left = node.left.left
                    right = node.left.right
                    node.value = node.left.value
                    node.setLeft(left)
                    node.setRight(right)
                    self._rotate(node, False)

                # когда есть только правый ребенок
                elif node.right:
                    left = node.right.left
                    right = node.right.right
                    node.value = node.right.value
                    node.setLeft(left)
                    node.setRight(right)
                    self._rotate(node, False)

                # когда нет детей
                else:
                    if node.parent:
                        if node.parent.left and node.parent.left.value == value:
                            node.parent.left = None
                        else:
                            node.parent.right = None
                        self._rotate(node.parent, False)
                    else:
                        self.root = None

            elif node.value > value:
                self._remove(node.left, value)
            else:
                self._remove(node.right, value)

    def _rotate(self, node: Node | None, is_add: bool = True):
        if node is None: return

        node.resetHeight()
        if abs(node.leftHeight - node.rightHeight) > 1:
            parent = node.parent
            if node.rightHeight > node.leftHeight:
                if node.right.rightHeight >= node.right.leftHeight:
                    node = self._rightRotate(node)
                else:
                    node.setRight(self._leftRotate(node.right))
                    node = self._rightRotate(node)
            else:
                if node.left.leftHeight >= node.left.rightHeight:
                    node = self._leftRotate(node)
                else:
                    node.setLeft(self._rightRotate(node.left))
                    node = self._leftRotate(node)

            if parent is None:
                node.parent = None
                self.root = node
            else:
                if parent.left == node.parent:
                    parent.setLeft(node)
                else:
                    parent.setRight(node)

            if is_add:
                return
        self._rotate(node.parent, is_add)

    @staticmethod
    def _rightRotate(node: Node) -> Node:
        left = node
        node = node.right
        left.setRight(node.left)
        node.setLeft(left)
        return node

    @staticmethod
    def _leftRotate(node: Node) -> Node:
        right = node
        node = node.left
        right.setLeft(node.right)
        node.setRight(right)
        return node
