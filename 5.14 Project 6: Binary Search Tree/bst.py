class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def is_empty(self):
        return self.root is None

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def add(self, item):
        self.root = self._add(self.root, item)

    def _add(self, node, item):
        if node is None:
            return Node(item)
        elif item < node.data:
            node.left = self._add(node.left, item)
        elif item > node.data:
            node.right = self._add(node.right, item)
        return node

    def remove(self, item):
        self.root = self._remove(self.root, item)

    def _remove(self, node, item):
        if node is None:
            return None
        if item < node.data:
            node.left = self._remove(node.left, item)
        elif item > node.data:
            node.right = self._remove(node.right, item)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.data = temp.data
                node.right = self._remove(node.right, temp.data)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find(self, item):
        return self._find(self.root, item)

    def _find(self, node, item):
        if node is None:
            raise ValueError("Item not found")
        elif item < node.data:
            return self._find(node.left, item)
        elif item > node.data:
            return self._find(node.right, item)
        else:
            return node.data

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        else:
            return self._inorder(node.left) + [node.data] + self._inorder(node.right)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        else:
            return [node.data] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        else:
            return self._postorder(node.left) + self._postorder(node.right) + [node.data]

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, depth):
        if node is not None:
            self._print_tree(node.left, depth + 1)
            print("   " * depth + str(node.data))
            self._print_tree(node.right, depth + 1)
