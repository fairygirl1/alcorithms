"""
Given the root of a Binary Search Tree (BST), 
return the minimum absolute difference between the 
values of any two different nodes in the tree.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(node):
            '''
            обход in-order - левое поддерево, 
            текущий узел, правое поддерево.

            вызывается для левого поддерева, 
            затем текущий узел добавляется в обход 
            (if node: ...), и если prev_val не является 
            None, то вычисляется разница между текущим 
            значением узла и prev_val, и эта разница 
            сравнивается с текущей min_diff. 
            '''
            nonlocal prev_val, min_diff
            if node:
                inorder(node.left)
                if prev_val is not None:
                    min_diff = min(min_diff, node.val - prev_val)
                prev_val = node.val
                inorder(node.right)

        prev_val = None
        min_diff = float('inf')
        inorder(root)
        return min_diff
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


solution = Solution()
result = solution.getMinimumDifference(root)
print(result)

