def counting_sort(input_list):

    count_elt = [0] * 10

    for number in input_list:
        count_elt[number] += 1

    total = 0
    for idx in range(10):
        old_elt = count_elt[idx]
        count_elt[idx] = total
        total += old_elt

    sorted_input_list = [0] * len(input_list)

    for number in input_list:
        sorted_input_list[count_elt[number]] = number
        count_elt[number] += 1

    return sorted_input_list


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input_list = counting_sort(input_list)

    first_number = 0
    second_number = 0

    for idx in range(len(sorted_input_list)-1, -1, -1):

        if idx % 2 == 0:
            first_number = first_number * 10 + sorted_input_list[idx]
        else:
            second_number = second_number * 10 + sorted_input_list[idx]

    return first_number, second_number


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# My tests
test_function([[], [0, 0]])
test_function([[6], [6, 0]])
test_function([[2, 2], [2, 2]])


