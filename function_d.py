def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

    # try commit without -m
    # try commit without -m second time

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
