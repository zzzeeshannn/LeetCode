# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Variable declaration 
        output = []
        curr_level = [root]
        
        while root and curr_level:
            curr_nodes = []
            next_level = []
            for all_nodes in curr_level:
                curr_nodes.append(all_nodes.val)
                if all_nodes.left:
                    next_level.append(all_nodes.left)
                if all_nodes.right:
                    next_level.append(all_nodes.right)
            output.append(curr_nodes)
            curr_level = next_level
        
        return output
            