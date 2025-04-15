from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            succ = self.get_successor(root)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)

        return root
    
    def get_successor(self, node):
        node = node.right
        while node is not None and node.left is not None:
            node = node.left
        return node 
    
