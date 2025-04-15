from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node: Node):
    if not node:
        return []
    q  = deque([node])
    res = []

    while q:
        node = q.popleft()
        res.append(node.value)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        

    return res