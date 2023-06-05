
# ненавижу этот алгоритм
def quick_sort(array: list, low_index: int, high_index: int) -> list:
    if low_index - high_index != 0:
        index = _split(array, low_index, high_index)
        quick_sort(array, low_index, index)
        quick_sort(array, index + 1, high_index)
    return array


def _split(array: list, low_index: int, high_index: int) -> int:
    result = low_index
    pivot = array[high_index - 1]
    for i in range(low_index, high_index):
        if array[i] > pivot: continue
        if i > result:
            array[result], array[i] = array[i], array[result]
        result += 1
    return result - 1
