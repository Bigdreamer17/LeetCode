class MyQueue:

    def __init__(self):
        self.d = deque()    

    def push(self, x: int) -> None:
        self.d.append(x)
        return None
    
    def pop(self) -> int:
        if len(self.d) > 0: 
            x = self.d.popleft()
            return x
        else:
            return None
    
    def peek(self) -> int:
        if len(self.d) > 0:
            return self.d[0]
        else:
            return None
    

    def empty(self) -> bool:
        if len(self.d) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()