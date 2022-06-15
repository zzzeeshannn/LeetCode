# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, left, right):
        if not left and not right: return True 
        if not left or not right: return False 
        return (left.val == right.val) and self.helper(left.left, right.right) and self.helper(left.right, right.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, root)
        
        