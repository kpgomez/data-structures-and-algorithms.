from data_structures.queue import Queue


def multi_bracket_validation(expr: str) -> bool:
    round_brackets = Queue()
    curly_brackets = Queue()
    square_brackets = Queue()
    empty = []

    for char in expr:
        if char == '(':
            round_brackets.enqueue(char)
        if char == '{':
            curly_brackets.enqueue(char)
        if char == '[':
            square_brackets.enqueue(char)
        if char == ')':
            if round_brackets.is_empty():
                return False
            else:
                round_brackets.dequeue()
        if char == '}':
            if curly_brackets.is_empty():
                return False
            else:
                curly_brackets.dequeue()
        if char == ']':
            if square_brackets.is_empty():
                return False
            else:
                square_brackets.dequeue()

    # confirm all queues are empty
    empty.append(round_brackets.is_empty())
    empty.append(curly_brackets.is_empty())
    empty.append(square_brackets.is_empty())
    return all(empty)

