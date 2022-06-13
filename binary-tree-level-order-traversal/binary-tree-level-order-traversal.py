# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Variable declaration here
        output = []
        currLevel = [root]
        
        while root and currLevel:
            currNodes = []
            nextLevel = []
            for every_node in currLevel:
                currNodes.append(every_node.val)
                if every_node.left:
                    nextLevel.append(every_node.left)
                if every_node.right:
                    nextLevel.append(every_node.right)
            output.append(currNodes)
            currLevel = nextLevel 
        
        return output