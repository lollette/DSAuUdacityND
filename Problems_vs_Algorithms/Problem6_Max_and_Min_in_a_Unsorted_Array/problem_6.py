import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        raise ValueError("ints list is empty")

    min = ints[0]
    max = ints[0]

    for i in range(1, len(ints)):

        if ints[i] < min:
            min = ints[i]
        elif ints[i] > max:
            max = ints[i]
    return min, max


# Example Test Case of Ten Integers

test_list = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_list)

print("Pass" if ((0, 9) == get_min_max(test_list)) else "Fail")

# My tests
try:
    get_min_max([])
except ValueError:
    print("Pass, the list is empty")

print("Pass" if ((9, 9) == get_min_max([9, 9])) else "Fail")
print("Pass" if ((0, 0) == get_min_max([0, 0])) else "Fail")
print("Pass" if ((-100, 0) == get_min_max([-1, -9, -100, 0, -20])) else "Fail")

