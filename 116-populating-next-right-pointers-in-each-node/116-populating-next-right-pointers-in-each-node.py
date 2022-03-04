"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Base case 
        if not root:
            return root
        
        # Variable declarations 
        queue = collections.deque()
        
        # Adding the root node to the queue
        queue.append(root)
        
        # Iterating over the queue
        while queue: 
            # Get the size
            size = len(queue)
            # Level order traversal 
            for i in range(size):
                # Obtain the node 
                currNode = queue.popleft()
                
                # Check for the next pointer node 
                if i < size - 1:
                    currNode.next = queue[0]
                
                if currNode.left:
                    queue.append(currNode.left)
                
                if currNode.right:
                    queue.append(currNode.right)
        
        return root