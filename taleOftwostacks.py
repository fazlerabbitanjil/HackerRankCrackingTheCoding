class MyQueue(object):
    def __init__(self):
        self.primary_stack = []
        self.secondary_stack = []

    def peek(self):
        return self.secondary_stack[-1]

    def pop(self):
        del self.primary_stack[0]
        self.sync_stacks()

    def put(self, value):
        self.primary_stack.append(value)
        self.sync_stacks()

    def sync_stacks(self):
        self.secondary_stack.clear()
        for item in reversed(self.primary_stack):
            self.secondary_stack.append(item)


            



queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
