from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
def reverse_string(string):
    stack = Stack()
    for i in string:
        stack.push(i)
    reversed_str = ''
    while stack.size() != 0:
        reversed_str += stack.pop()
    return reversed_str

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(10)
    print(s.pop())
    print(s.peek())

    print(reverse_string("We won the match"))
