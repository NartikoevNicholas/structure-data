
# O(n^2)
def insert_sort(array: list) -> list:
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            value = array[j]
            array[j] = array[j - 1]
            array[j - 1] = value
            j -= 1
    return array
