class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)

    def pop(self) -> None:
        self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.MinStack[-1]

        while len(self.MinStack):
            mini = min(mini, self.MinStack[-1])
            tmp.append(self.MinStack.pop())

        while len(tmp):
            self.MinStack.append(tmp.pop())

        return mini
