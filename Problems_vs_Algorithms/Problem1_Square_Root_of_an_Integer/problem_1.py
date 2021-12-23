def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if not isinstance(number, int) or number < 0:
        return "Unknown number"

    if number == 0 or number == 1:
        return number
    start = 1
    end = int(number / 2)
    while start <= end:
        middle = (start + end) // 2
        if middle * middle == number:
            return middle
        if middle * middle < number:
            start = middle + 1
            root = middle
        else:
            end = middle - 1
    return root


print("Pass" if(3 == sqrt(9)) else "Fail")
print("Pass" if(0 == sqrt(0)) else "Fail")
print("Pass" if(4 == sqrt(16)) else "Fail")
print("Pass" if(1 == sqrt(1)) else "Fail")
print("Pass" if(5 == sqrt(27)) else "Fail")


# My tests
print ("Pass" if("Unknown number" == sqrt(-9)) else "Fail")
print ("Pass" if("Unknown number" == sqrt(9.5)) else "Fail")
print ("Pass" if(608154 == sqrt(369852417852)) else "Fail")
print ("Pass" if("Unknown number" == sqrt('foo')) else "Fail")

