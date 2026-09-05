from collections import deque
class MinStack:

    def __init__(self):
        self.ans = deque()
        self.mins = deque()

    def push(self, value: int) -> None:
        self.ans.append(value)

        if not self.mins or value <= self.mins[-1]:
            self.mins.append(value)

    def pop(self) -> None:
        value = self.ans.pop()

        if value == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.ans[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()