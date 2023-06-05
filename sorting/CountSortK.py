

def count_sort_k(array: list, m: int):
    result = []
    new_array = []
    first_max = second_max = 0
    for el in array:
        b = int(el / m)
        c = el - b * m
        new_array.append((b, c))
        if b > first_max: first_max = b
        if c > second_max: second_max = c

    first_sort = _sort(new_array, first_max, 1)
    second_sort = _sort(first_sort, second_max, 0)

    for el in second_sort:
        result.append(el[0] * m + el[1])
    return result


def _sort(array: list, m: int,  pos: int) -> list:
    result = [0] * len(array)

    cnt = [0] * (m + 1)
    for el in array:
        val = el[pos]
        cnt[val] += 1

    p = [0] * (m + 2)
    for index, el in enumerate(cnt):
        p[index + 1] = p[index] + el

    for el in array:
        val = el[pos]
        result[p[val]] = el
        p[val] += 1

    return result
