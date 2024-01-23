def reverse_array(arr):
    counter = 0

    def find_length(arr):
        length = 0
        for item in arr:
            length += 1
        return length

    arr_length = find_length(arr)
    reverse_list = [element for element in arr]

    for element in arr:
        counter -= 1
        reverse_list[arr_length + counter] = element

    return reverse_list
