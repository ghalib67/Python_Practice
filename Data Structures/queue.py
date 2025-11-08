class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"



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


class linkedQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def enqueue(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node 
            self.tail = node
            self.length += 1
            return
        
        self.tail.next = node
        self.tail = node
        self.length += 1
        
    def dequeue(self):
        if self.length != 0:
            self.head = self.head.next
            self.length -= 1
            return
        
        raise IndexError("Cant dequeue an empty list")
    
    def peek(self):
        if self.length != 0:
            print(self.head)
            return self.head
        raise IndexError("Cant peek at an empty list")
    
    def isEmpty(self):
        return self.length == 0
    
    def display(self):
        if self.length == 0:
            print("There queue is empty")
            return
        current = self.head
        while current is not None:
            print(f"{current} ",end= "")
            if current.next is not None:
                print("<- ",end="")
            current = current.next
        print()
    
    
if __name__ == "__main__":
    q = linkedQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()
    q.peek()
