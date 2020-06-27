class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.elements = []
        self.head = None
        self.tail = None

    def add_list(self):
        self.elements = []
        current = self.head
        while current.next is not None:
            self.elements.append(current.value)
            current = current.next
        self.elements.append(current.value)



    def append(self, item):
        if self.length <= self.capacity:
            if self.head is None:
                new_node = Node(item)
                self.head = new_node
                self.tail = new_node
                self.length += 1
            elif self.head == self.tail:
                new_node = Node(item)
                self.head = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
                self.length += 1
                self.add_list()
            else:
                new_node = Node(item)
                old_node = self.head
                self.head = new_node
                self.head.next = old_node
                old_node.prev = self.head
                self.length += 1
                self.add_list()
        else:
            new_node = Node(item)
            old_node = self.tail
            old_head = self.head
            self.head = old_head.next
            self.head.prev = None
            self.tail = new_node
            self.tail.prev = old_node
            old_node.next = self.tail
            self.add_list()


    def get(self):
        return self.elements
