# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def max_gain(self, root):
        
        if not root:
                return 0
        # max sum on the left and right sub-trees of node
        left_gain = max(self.max_gain(root.left), 0)
        right_gain = max(self.max_gain(root.right), 0)
            
        # the price to start a new path where `node` is a highest node
        price_newpath = root.val + left_gain + right_gain
            
        # update max_sum if it's better to start a new path
        self.max_sum = max(self.max_sum, price_newpath)
        
        # for recursion :
        # return the max gain if continue the same path
        return root.val + max(left_gain, right_gain)
        

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float("-inf")
        self.max_gain(root)
        return self.max_sum