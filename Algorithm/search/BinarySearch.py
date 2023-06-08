

def binary_search_index(array: list, value: int):
    left, right = -1, len(array)
    while right - left > 1:
        index = int((right + left) / 2)
        if value > array[index]:
            left = index
        else:
            right = index
    return right
