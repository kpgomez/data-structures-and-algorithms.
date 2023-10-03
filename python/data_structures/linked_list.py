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
        # method body here
        if self.head is None:
            self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head

    def includes(self, value):
        # method body here
        if self.head.value:
            return True
        else:
            return False

    def __str__(self):
        # method body here
        current = self.head
        # print(current) # shows a memory address, <data_structures.linked_list.Node object at 0x10505dc10>
        # print(current.value) # shows apple
        # print(current.next) # shows None

        if current is None:
            return "NULL"

        linked_list_values = []

        while current:
            # (f"{{ {current.value} }} -> NULL") # shows { apple } -> NULL
            # performs logic
            linked_list_values.append(current.value)
            current = current.next

        # need this to be more dynamic, can't figure it out atm
        if(len(linked_list_values) == 1):
            return(f"{{ {linked_list_values[0]} }} -> NULL")
        if(len(linked_list_values) == 2):
            return(f"{{ {linked_list_values[0]} }} -> {{ {linked_list_values[1]} }} -> NULL")

        # for value in linked_list_values:
        #     return f"{{ {value} }}"






class TargetError:
    pass
