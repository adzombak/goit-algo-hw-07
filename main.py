class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key < node.val:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node


def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


def sum_nodes(node):
    if node is None:
        return 0
    return node.val + sum_nodes(node.left) + sum_nodes(node.right)


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    print(min_value(root))
    print(max_value(root))
    print(sum_nodes(root))
