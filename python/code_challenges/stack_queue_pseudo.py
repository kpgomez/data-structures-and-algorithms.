from data_structures.stack import Stack


# https://chat.openai.com/c/2f646257-a994-49ef-ac80-4a4d6b5cf60e
class PseudoQueue:
    def __init__(self):
        # create two instances of a Stack, one for enqueueing and one for dequeueing
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, value):
        # push new value into the in_stack
        self.in_stack.push(value)

    def dequeue(self):
        # first check if out_stack is empty
        if not self.out_stack.top:
            # while in_stack is not empty
            while self.in_stack.top:
                # first pops the top value of in_stack then push that value into the out_stack,
                # essentially reversing the order
                self.out_stack.push(self.in_stack.pop())
        # once the stack out_stack finishes reversing the order of what was once the in_stack,
        # assign the top value of the out_stack to a ref
        oldest = self.out_stack.pop()
        while self.out_stack.top:
            # move nodes from dequeue back onto enqueue as per the lecture
            self.in_stack.push(self.out_stack.pop())
        return oldest
