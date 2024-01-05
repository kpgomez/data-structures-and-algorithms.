def merge_sort(arr: list[int]) -> list[int]:
    """

    :param arr:
    :type arr:
    :return:
    :rtype:
    """
    n = len(arr)

    if n > 1:
        mid = n//2
        print(mid)
        left = arr[0:mid]
        print('left', left)
        right = arr[mid:n]
        print('right', right)

        merge_sort(left)
        merge_sort(right)
        return merge(left, right, arr)


def merge(left: list[int], right: list[int], arr: list[int]) -> list[int]:
    """
    Helper method to combine sorted left and right half
    :param left: sorted list of integers from the left half of original list of integers
    :type left: list[int]
    :param right: sorted list of integers from the right half of original list of integers
    :type right: list[int]
    :param arr: original input list of integers
    :type arr: list[int]
    :return: a new list of integers sorted in ascending order
    :rtype: list
    """
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        arr[k] = right[j]
        # k += 1
        # j += 1
    else:
        arr[k] = left[i]
        # k += 1
        # i += 1

    return arr


if __name__ == "__main__":
    # print(merge_sort([8, 4, 23, 42, 16, 15]))
    reverse_sorted = [20, 18, 12, 8, 5, -2]
    reverse_sorted_remix = [18, 12, 8, 5, -2, 20]
    print(merge_sort(reverse_sorted))  # should result [-2, 5, 8, 12, 18, 20] but tests show [-2, 5, 8, 12, 5, -2]
    print(merge_sort(reverse_sorted_remix)) # resulted in [-2, 5, 8, 12, 18, 20] which is correct, only difference
    # is this one does not start with the largest value

    # few_uniques = [5, 12, 7, 5, 5, 7]
    # print(merge_sort(few_uniques))  # should result [5, 5, 5, 7, 7, 12] but tests show [5, 5, 5, 7, 7, 7]
    # nearly_sorted = [2, 3, 5, 7, 13, 11]
    # print(merge_sort(nearly_sorted))  # should result [2, 3, 5, 7, 11, 13] but tests show [2, 3, 5, 7, 13, 11]
