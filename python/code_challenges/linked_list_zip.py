from data_structures.linked_list import LinkedList

# https://chat.openai.com/c/66fef8fb-4ee0-4032-9296-a44106e5d6f0
def zip_lists(list1, list2):
    list3 = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 or current2:
        if current1:
            list3.append(current1.value)
            current1 = current1.next
        if current2:
            list3.append(current2.value)
            current2 = current2.next

    return list3
