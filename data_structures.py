class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, new_item):
        self.items.append(new_item)
    
    def pop(self):
        items = self.items
        return items.pop(len(items) - 1)

    def peek(self):
        return self.items[-1]

if __name__ == "__main__":
    pancake = Stack()
    pancake.push("butter")
    pancake.push("syrup")
    print(pancake.items)
    print(pancake.pop())
    print(pancake.items)
    print(pancake.peek())
    print(pancake.items)
    