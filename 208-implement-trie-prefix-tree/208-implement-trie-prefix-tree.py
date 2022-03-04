class Node:
    
    def __init__(self):
        self.final = False
        self.children = dict()

class Trie:

    def __init__(self):
        self._node = Node()
        

    def insert(self, word: str) -> None:
        node = self._node
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
                
            node = node.children[ch]
            
        node.final = True
        

    def search(self, word: str) -> bool:
        node = self._node
        
        for ch in word:
            if ch not in node.children:
                return False
            
            node = node.children[ch]
            
        return node.final
        

    def startsWith(self, prefix: str) -> bool:
        node = self._node
        
        for ch in prefix:
            if ch not in node.children:
                return False
            
            node = node.children[ch]
            
        return True