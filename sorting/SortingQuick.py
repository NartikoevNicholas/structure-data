
# ненавижу этот алгоритм
def sorting_quick(array: list, low_index: int, high_index: int) -> list:
    if low_index - high_index != 0:
        index = split(array, low_index, high_index)
        sorting_quick(array, low_index, index)
        sorting_quick(array, index + 1, high_index)
    return array


def split(array: list, low_index: int, high_index: int) -> int:
    result = low_index
    pivot = array[high_index - 1]
    for i in range(low_index, high_index):
        if array[i] > pivot: continue
        if i > result:
            array[result], array[i] = array[i], array[result]
        result += 1
    return result - 1
