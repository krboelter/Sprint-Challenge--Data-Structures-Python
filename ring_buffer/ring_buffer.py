class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = []
        self.pointer = 0


    # add pointer
    def append(self, item):
        
        # if length of array is less than capacity...
        if len(self.elements) < self.capacity:
            self.elements.append(item)
            self.pointer += 1
        # if pointer value is less than or equal to capacity...
        elif self.pointer < self.capacity:
            self.elements.pop(self.pointer)
            self.elements.insert(self.pointer, item)
            self.pointer += 1
        # if pointer value is greater than capacity...
        else:
            self.pointer = 0
            self.elements.pop(self.pointer)
            self.elements.insert(self.pointer, item)
            self.pointer += 1


    def get(self):
        return self.elements
