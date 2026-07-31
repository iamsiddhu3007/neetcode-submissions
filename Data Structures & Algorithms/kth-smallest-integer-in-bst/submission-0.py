# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## inorder travesal gives the sorter list
        def dfs(node, stack):
            if not node:
                return
            dfs(node.left, stack)
            stack.append(node.val)
            dfs(node.right, stack)
            return
        stack = []
        dfs(root, stack)
        
        return stack[k-1]

        
          