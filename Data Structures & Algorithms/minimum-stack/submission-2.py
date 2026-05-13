class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            prev = self.stack[-1]
            cur_min = min(val, prev[1])
            self.stack.append((val, cur_min))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            return top[0]
        return None

    def getMin(self) -> int:
        if self.stack:
            top = self.stack[-1]
            return top[1]
        return None
        
