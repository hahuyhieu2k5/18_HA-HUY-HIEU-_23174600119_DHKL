class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print("Ngăn xếp đã đầy")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Ngăn xếp rỗng")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size


    def count(self):
        return len(self.items)

stack = Stack(6)
stack.push(2.1)
stack.push(3.9)
print(stack.count()) 