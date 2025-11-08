class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    inputs = ["push 10", "push 20", "push 30", "peek", "pop", "peek", "pop", "pop"]
    for cmd in inputs:
        parts = cmd.split()
        if parts[0] == "push":
            s.push(parts[1])
            print(f"Pushed {parts[1]}")
        elif parts[0] == "pop":
            try:
                print(f"Popped: {s.pop()}")
            except IndexError as e:
                print(e)
        elif parts[0] == "peek":
            try:
                print(f"Top: {s.peek()}")
            except IndexError as e:
                print(e)
