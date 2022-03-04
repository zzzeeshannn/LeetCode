class MyQueue:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.temp_stack = []
      
        while self.stack:
            self.temp_stack.append(self.stack.pop())
       
        result = self.temp_stack.pop()
        
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())
        
        return result 
    
    def peek(self) -> int:
        if len(self.stack) > 0:
            return self.stack[0]
        else:
            return -1

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True 
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()