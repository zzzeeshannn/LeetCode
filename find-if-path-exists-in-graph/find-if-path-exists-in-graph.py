class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # Variable declaration
        adjacency_list = [[] for _ in range(n)]
        queue = collections.deque()
        seen = set()
        
        # Since we have a list of edges here, generate a adjacency list 
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        
        # Add the starting node to the queue and set of seen nodes
        queue.append(start)
        seen.add(start)
        
        while queue:
            # Retrieve a node 
            currNode = queue.popleft()
            
            if currNode == end:
                return True
            
            for every_neighbour in adjacency_list[currNode]:
                if every_neighbour not in seen:
                    seen.add(every_neighbour)
                    queue.append(every_neighbour)
        
        return False