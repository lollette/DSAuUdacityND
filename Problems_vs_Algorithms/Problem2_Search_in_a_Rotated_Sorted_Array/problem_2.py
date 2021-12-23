def binary_search_pivot(input_list, start, end):
    if end < start:
        return -1

    if end == start:
        return start

    middle = int((start + end) / 2)

    if middle < end and input_list[middle] > input_list[middle + 1]:
        return middle

    if middle > start and input_list[middle] < input_list[middle - 1]:
        return middle - 1

    if input_list[start] >= input_list[middle]:

        return binary_search_pivot(input_list, start, middle - 1)

    return binary_search_pivot(input_list, middle + 1, end)


def binary_search(input_list, start, end, number):
    if end < start:
        return -1

    middle = int((start + end) / 2)

    if number == input_list[middle]:
        return middle

    if number > input_list[middle]:
        return binary_search(input_list, (middle + 1), end, number)

    return binary_search(input_list, start, (middle - 1), number)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1

    pivot = binary_search_pivot(input_list, 0, len(input_list) - 1)

    if pivot == -1:
        return binary_search(input_list, 0, len(input_list) - 1, number)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)

    return binary_search(input_list, pivot + 1, len(input_list) - 1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# My tests

test_function([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 10])
test_function([[], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 100])
test_function([[6, 7, 8, 9, 10, -2, -1, 3, 4], -1])
test_function([[-6, -2, -1, 3, 4, 9, -10, -8, -7], 3])
