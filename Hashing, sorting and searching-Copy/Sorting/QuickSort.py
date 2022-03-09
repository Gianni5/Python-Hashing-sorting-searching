from ListNumbers.UnsortedNumbers import *

def quicksort(array):
    """
    quick sorting function
    :param array:
    :return:
    """
    length = len(array)
    if length <= 1:
        return array
    else:
        a = length // 2  # getting the middle of the array
        middle = array.pop(a)  # assigning the middle of the array
        left = []
        right = []
    for i in array:  # loop throw
        if i < middle:
            left.append(i)  # if the value is less then middle append to the left array
        else:
            right.append(i)  # if the value is greater then middle append to the right array
    return quicksort(left) + [middle] + quicksort(right)


sorted_number = quicksort(numbers_list)
print(sorted_number)
