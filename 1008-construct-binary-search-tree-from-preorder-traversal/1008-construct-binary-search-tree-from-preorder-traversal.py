# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for v in preorder[1:]:
            node = TreeNode(v)
            if node.val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and node.val > stack[-1].val:
                    l = stack.pop()
                l.right = node
            stack.append(node)
        return root