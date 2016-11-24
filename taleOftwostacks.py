class MyQueue(object):
    def __init__(self):
        self.primary_stack = []
        self.secondary_stack = []

        pass
    def peek(self):
        pass

    def pop(self):
        pass

    def put(self, value):
        pass

    def sycn_stacks(ps,ss):
        for val in ps:
            pass
            



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
