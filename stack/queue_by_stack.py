class QueueByStack:
    def __init__(self):
        self.stack_for_enqueue = []
        self.stack_for_dequeue = []

    def enqueue(self, x):
        self.stack_for_enqueue.append(x)

    def dequeue(self):
        if self.stack_for_dequeue:
            return self.stack_for_dequeue.pop()
        elif not self.stack_for_enqueue:
            raise Exception
        
        while self.stack_for_enqueue:
            self.stack_for_dequeue.append(self.stack_for_enqueue.pop())
        return self.stack_for_dequeue.pop()
