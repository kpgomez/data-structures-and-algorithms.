def sum_rows(matrix: list[list[any]]) -> list[int]:
    all_sums = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], int):
                sum += matrix[i][j]
        all_sums.append(sum)
    return all_sums
