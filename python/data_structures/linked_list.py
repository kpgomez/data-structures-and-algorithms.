class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def insert(self, value):
        """

        """
        if self.head is None:
            self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head

    def includes(self, value):
        """

        """
        current = self.head

        linked_list_values = []

        while current:
            linked_list_values.append(current.value)
            current = current.next

        if value in linked_list_values:
            return True
        else:
            return False

    def __str__(self):
        # method body here
        current = self.head

        if current is None:
            return "NULL"

        linked_list_values = ""

        while current:
            # performs logic
            linked_list_values += f"{{ {current.value} }} -> "
            current = current.next

        return linked_list_values + 'NULL'

    def append(self, value):
        """

        """
        ## my attempt
        # current = self.head
        # while current:
        #     current = current.next
        # # new_node = Node(value)
        # current.next = Node(value)

        #with help from ChatGPT
        ## step one - instantiate new node
        new_node = Node(value)

        ## step two - make new node the head if this is a new linked list
        if self.head is None:
            self.head = new_node
            return

        ## you have to traverse linked list starting at the head
        current = self.head

        ## looks like my attempt was missing .next
        while current.next:
            current = current.next

        ## change the pointer to now point to new_node
        current.next = new_node

class TargetError:
    pass
