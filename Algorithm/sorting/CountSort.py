

def count_sort(array: list) -> list:
    result = []
    cnt = [0] * (max(array) + 1)  #
    for el in array:
        cnt[el] += 1

    for index, value in enumerate(cnt):
        for i in range(value):
            result.append(index)

    return result
