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
            # +1은 현재 노드
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
        # 노드가 0이거나 적절한 위치에 도달
        if node is None:
            return Node(item)
        '''BST에서는 각 노드의 왼쪽 서브트리에 있는 모든 노드의 값이 해당 노드의 값보다 작아야 하며, 
        오른쪽 서브트리에 있는 모든 노드의 값이 해당 노드의 값보다 커야 합니다.'''
        elif item < node.data:
            node.left = self._add(node.left, item)
        elif item > node.data:
            node.right = self._add(node.right, item)
        return node

    def remove(self, item):
        self.root = self._remove(self.root, item)

    def _remove(self, node, item):
        # 노드가 비었거나 특정 아이템 못찾으면
        if node is None:
            return None
        if item < node.data:
            node.left = self._remove(node.left, item)
        elif item > node.data:
            node.right = self._remove(node.right, item)
        # 제거 아이템이 현재 노드 데이터와 같은 경우
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # 두개 자식 모두 있음
            else:
                # 오른쪽 서브트리에서 가장 작으거 찾아
                temp = self._find_min(node.right)
                # 현제 노드 데이터를 가장 작은거로 교체
                node.data = temp.data
                # 그거를 오른쪽에서 제거
                node.right = self._remove(node.right, temp.data)
        return node

    # 주어진 노드 서브트리에서 가장 작은 노드 찾기
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
        # 트리가 비었거나 방문했으면
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
