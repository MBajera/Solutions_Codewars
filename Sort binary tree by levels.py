class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    array = []
    to_check = [node]
    while to_check:
        if isinstance(to_check[0], Node):
            if to_check[0].value is not None:
                array.append(to_check[0].value)
            for child in [to_check[0].left, to_check[0].right]:
                if child is not None:
                    to_check.append(child)
        to_check.pop(0)
    return array
