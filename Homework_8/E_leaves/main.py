class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root, 1)

    def _insert(self, value, cur_node, cnt):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                cnt += 1
                self._insert(value, cur_node.left, cnt)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                cnt += 1
                self._insert(value, cur_node.right, cnt)

    def in_order_leafs(self):
        in_order_values = []
        if self.root is not None:
            return self._in_order_leafs(self.root, in_order_values)

    def _in_order_leafs(self, cur_node, in_order_values):
        if cur_node is not None:
            self._in_order_leafs(cur_node.left, in_order_values)
            if cur_node.left is None and cur_node.right is None:
                in_order_values.append(cur_node.value)
            self._in_order_leafs(cur_node.right, in_order_values)
        return in_order_values


values = list(map(int, input().split()))[:-1]
tree = BinarySearchTree()
for value in values:
    tree.insert(value)
for element in tree.in_order_leafs():
    print(element)
