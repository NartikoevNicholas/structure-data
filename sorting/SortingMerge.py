

# O(nlogn)
def sort_merge(array: list) -> list:
    n = len(array)

    if n <= 1:
        return array

    first_array = sort_merge(array[:int(n/2)])
    second_array = sort_merge(array[int(n/2):])
    return merge(first_array, second_array)


def merge(a: list, b: list) -> list:
    result = []

    a_len = len(a)
    b_len = len(b)

    a_index = 0
    b_index = 0

    while a_index < a_len or b_index < b_len:
        if a_index < a_len and b_index < b_len:
            if a[a_index] < b[b_index]:
                result.append(a[a_index])
                a_index += 1
            else:
                result.append(b[b_index])
                b_index += 1
        elif a_index < a_len:
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1

    return result
