

def bubble_sort(array: list) -> list:
    lenght = len(array)
    while lenght > 0:
        for i in range(lenght - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        lenght -= 1

    return array


