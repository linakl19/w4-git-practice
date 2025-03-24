def merge_lists(list_a, list_b):
    new_list = list_a.append(list_b)
    return new_list


if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
