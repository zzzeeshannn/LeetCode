class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ''
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, path, is_file, content=''):
        curr = self.root
        
        for level in path.strip('/').split('/'):
            if level not in curr.children:
                curr.children[level] = TrieNode()
            curr = curr.children[level]
        
        if is_file:
            curr.is_file = True
            
            if content:
                curr.content = content
        
    def search(self, path):
        curr = self.root
        
        if path != '/':
            for level in path.strip('/').split('/'):
                if level not in curr.children:
                    return []
                curr = curr.children[level]
            
        if curr.is_file:
            return [path.split('/')[-1]]
        else:
            return sorted(curr.children)
        
    def read(self, path):
        curr = self.root
        
        for level in path.strip('/').split('/'):
            if level not in curr.children:
                return ''
            curr = curr.children[level]
            
        return curr.content
                 

class FileSystem:
    def __init__(self):
        self.fs = Trie()

    def ls(self, path: str) -> List[str]:
        return self.fs.search(path)
        
    def mkdir(self, path: str) -> None:
        self.fs.insert(path, is_file=False)
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        file_content = self.fs.read(filePath)
        self.fs.insert(filePath, is_file=True, content=file_content+content)
             
    def readContentFromFile(self, filePath: str) -> str:
        return self.fs.read(filePath)