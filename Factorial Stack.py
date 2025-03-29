class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
    def is_full(self):
        return len(self.stack) >= self.size
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        if self.is_full():
            return "STACK OVERFLOW"
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            return "STACK UNDERFLOW"
        return self.stack.pop()
def factorial_with_stack(n):
    if n == 0:
        return "FACTORIAL IS : 1"
    max_stack_size = 100
    stack = Stack(max_stack_size) 
    result = 1
    for i in range(1, n + 1):
        if stack.push(i) == "STACK OVERFLOW":
            return "STACK OVERFLOW"
    while not stack.is_empty():
        result *= stack.pop()
    return f"FACTORIAL IS : {result}"
try:
    n = int(input("Enter a number: "))
    print(factorial_with_stack(n))
except ValueError:
    print("Please enter a valid integer.")