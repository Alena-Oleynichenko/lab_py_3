import json


def read_data(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as read_file:
        lst = json.load(read_file)
    return lst


def shell_sort(lst: list) -> list:
    second = len(lst) - 1
    gap = len(lst) // 2
    while gap > 0:
        for value in range(gap, len(lst), 1):
            j = value
            position = j - gap

            while position >= 0 and lst[position]['weight'] > lst[j]['weight']:
                lst[position], lst[j] = lst[j], lst[position]
                j = position
                position = j-gap
        gap //= 2
    return lst


def serialization(local_data: list, path: str) -> None:
    with open(path, 'w') as file:
        json.dump(local_data, file)


def deserialization(path: str) -> list:
    with open(path, 'r') as file:
        local_data = json.load(file)
    return local_data
