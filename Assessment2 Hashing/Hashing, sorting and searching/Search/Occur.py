def occurrences(lis, target):
    """
    function to check how many time the number occur in a list
    :param lis: list
    :param target:
    :return: returning the count
    """
    count = 0
    for n in lis:  # searching fo the numbers
        if n == target:
            count += 1  # add 1 every time the number occur
    return count
