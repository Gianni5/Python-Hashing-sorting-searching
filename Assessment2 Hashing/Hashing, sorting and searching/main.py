from Sorting.QuickSort import *
from Hashing.Hash import *
from Search.BinarySearch import Search
from Search.Occur import occurrences
if __name__ == "__main__":
    print(sorted_number)
    my_object = HashTable(sorted_number)
    for x in sorted_number:
        my_object.add(x)
    my_object.print()

    binary = Search()

    print("*" * 50, " SEARCHING THE NUMBER ", "*" * 50)
    while True:
        user_input = input("please insert a number:")
        try:
            int(user_input)
            result = binary.binary_search(sorted_number, user_input)
            print('{} has occurred {} times'.format(user_input, occurrences(sorted_number, result)))
        except ValueError:
            print("please insert number value")
            break
