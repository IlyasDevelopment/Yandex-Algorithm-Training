class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.heights = []

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.heights.append(1)
        else:
            self._insert(value, self.root, 1)

    def _insert(self, value, cur_node, cnt):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
                self.heights.append(cnt+1)
            else:
                cnt += 1
                self._insert(value, cur_node.left, cnt)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
                self.heights.append(cnt+1)
            else:
                cnt += 1
                self._insert(value, cur_node.right, cnt)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)


values = list(map(int, input().split()))[:-1]
tree = BinarySearchTree()
for value in values:
    tree.insert(value)
print(*tree.heights)
