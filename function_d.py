def max_value(numbers):
    numbers = [2,3,4,5]
    sum = 0
    for num in numbers:
        sum += num
    return sum


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
