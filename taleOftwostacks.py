class MyQueue(object):
    def __init__(self):
        self.primary_stack = []
        self.secondary_stack = []

    def peek(self):
        if len(self.secondary_stack) > 0:
            return self.secondary_stack[-1]
        else:
            self.sync_stacks()
            return self.secondary_stack[-1]

    def pop(self):
        if len(self.secondary_stack) > 0:
            self.secondary_stack.pop()
            del self.primary_stack[0]
        else:
            self.sync_stacks()
            self.secondary_stack.pop()
            del self.primary_stack[0]

    def put(self, value):
        self.primary_stack.append(value)
       # self.sync_stacks()

    def sync_stacks(self):
        #print("syncing")
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
