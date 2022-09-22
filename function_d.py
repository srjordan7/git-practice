def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    highest = 0
    for num in numbers:
        if num > highest:
            highest = num
    return highest
    print("How are you?")


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
