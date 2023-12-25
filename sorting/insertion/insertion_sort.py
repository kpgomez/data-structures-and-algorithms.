def insert(sorted: list[int], value: int) -> None:
    """
    Helper method for insertion sort that finds correct position for unsorted value
    :param sorted: list of previously sorted integers
    :type sorted: list
    :param value: unsorted value
    :type value: int
    :return: None
    :rtype: is also None
    """
    i = 0
    # https://chat.openai.com/c/734aa88c-6ed1-4b7d-80d5-20fe5ed66ad7
    while i < len(sorted) and value > sorted[i]:
        i += 1
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i += 1
    sorted.append(value)


def insertion_sort(input: list[int]) -> list[int]:
    """
    Sorting method that traverses entire input list and checks each value one by one to find its correct position
    :param input: list of integers
    :type input: list
    :return: list of sorted integers
    :rtype: list
    """
    if len(input) <= 0:
        return []
    # https://datascienceparichay.com/article/python-check-if-all-elements-in-list-are-integers/
    if all(isinstance(item, int) for item in input):
        sorted = [input[0]]
        for i in range(1, len(input)):
            insert(sorted, input[i])
        return sorted
    else:
        return "Cannot sort because input list contains non-integer values"


if __name__ == "__main__":

    print(insertion_sort(test_list))
