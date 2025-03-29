class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def generate_fibonacci(n):
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    return fib
def create_linked_list(n):
    head = Node('A')
    current = head
    for i in range(1, n):
        current.next = Node(chr(ord('A') + i))
        current = current.next
    return head
def delete_nodes(head, fib_sequence):
    current = head
    prev = None
    index = 0
    while current:
        if index in fib_sequence:
            if prev:
                prev.next = current.next
            else:
                head = current.next
        else:
            prev = current
        current = current.next
        index += 1
    return head
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
n = int(input())
fib_sequence = generate_fibonacci(n)
head = create_linked_list(fib_sequence[-1])
head = delete_nodes(head, fib_sequence)
print_linked_list(head)