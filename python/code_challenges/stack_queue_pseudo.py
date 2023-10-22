from data_structures.stack import Stack


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class PseudoQueue:
    def __init__(self, front=None, rear=None):
        self.front = rear # when there is a single node, both front and rear point to same node
        self.rear = rear

    def enqueue(self, value: str) -> None:
        """
        Inserts a value into the PseudoQueue, using a FIFO approach
        :param value: a string representing value to be added to PseudoQueue
        :return: None
        """
        pass

    def dequeue(self) -> str:
        """
        Extracts a value from the PseudoQueue, using a FIFO approach
        :return: a string representing the value removed from the PseudoQueue
        """
        pass


