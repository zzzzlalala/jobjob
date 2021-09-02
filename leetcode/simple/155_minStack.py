class Minstack:
    def __init__(self):
        self.stack = []
        self.minstack = [float("inf")]

    def push(self, x):
        self.stack.append(x)
        self.minstack.append(min(x, self.minstack[-1]))

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]
