class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class linkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self,data,index = None):
        new_node = Node(data)
        if index == None or index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                print("Index is out of bounds")
                return
            current = current.next
        if current is None:
            print("index out of range")
            return
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        
    def treverse(self,nodes = None):
        if self.length > 0:
            print("| ",end="")
            current = self.head
            for i in range(self.length - 1 if nodes is None else nodes - 1):
                print(f"{current} -> ",end="")
                current = current.next
                if current.next is None:
                    print(f"{current} -> None |")
                    if  nodes is not None and nodes > self.length:
                        print(f"The given value {nodes} was out of bounds, could display upto{self.length}")         
            return
        print("The list is empty :[")
        
Linked_List = linkedList()
for i in range(15):
    Linked_List.insert(i)
Linked_List.treverse()

