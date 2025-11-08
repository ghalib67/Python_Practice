class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Nothing to remove.")
            return None
        removed = self.items.pop(0)
        print(f"{removed} removed from the queue.")
        return removed

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front of queue: {self.items[0]}")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents:", " <- ".join(map(str, self.items)))


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.peek()
    q.dequeue()
    q.display()
