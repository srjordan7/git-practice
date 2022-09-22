def most_common_value(number_list):
    """ returns the most common element of the list
    """
    most_common_count = 0
    current_count = 0
    most_common_value = None
    for num in nums:
        current = num
        for num in nums:
            if num == current:
                current_count += 1
        if current_count > most_common_count:
            most_common_value = current
    return most_common_value




if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
