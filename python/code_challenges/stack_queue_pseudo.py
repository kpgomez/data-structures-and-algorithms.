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
        # first check if it is the top
        if not self.out_stack.top:
            # while truthy or top is not None so basically the entire length of the in_stack
            while self.in_stack.top:
                # first pops the top value of in_stack then push that value into the out_stack,
                # this essentially reverses the order of the stack from newest value on top to
                # now oldest value on top
                self.out_stack.push(self.in_stack.pop())
        # once the stack out_stack reverses the order of what was once the in_stack,
        # return the top value of the out_stack
        return self.out_stack.pop()
