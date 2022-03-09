from collections import OrderedDict, Counter
from math import sqrt

my_number = "36 29 31 125 139 131 115 105 111 40 119 47 105 57 122 109 124 115 43 120 43 27 27 32 61 37 \
127 29 113 121 58 114 126 53 114 96 12 127 28 42 39 113 42 18 44 18 28 48 125 107 114 34 133 \
45 120 30 127 31 116 146 58 109 23 105 63 27 44 105 99 41 128 121 116 125 118 44 37 113 124 \
37 48 127 25 109 7 31 141 46 13 27 43 117 116 27 7 68 40 31 115 124 42 128 52 71 118 117 38 \
27 106 33 117 116 132 104 123 35 113 122 42 117 119 32 61 37 127 29 113 121 58 114 126 53 \
114 96"

numbers_list = my_number.split(' ')

for i in range(0, len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])


def quicksort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        a = length // 2
        middle = array.pop(a)
        left = []
        right = []
    for i in array:
        if i < middle:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [middle] + quicksort(right)


sorted_number = quicksort(numbers_list)
print(sorted_number)
print('*' * 100)


def tree_stem(number):
    stem = []
    for x in number:

        s = (str(x)[:-1])
        if s == '':
            s = 0
        stem.append(int(s))
        # print(stem)
    return stem


stems = tree_stem(sorted_number)
print(stems)

print('-' * 50)


def tree_leaf(number):
    leaf = []
    for x in number:
        l = str(x)[-1]
        leaf.append(int(l))
    return leaf


leafs = tree_leaf(sorted_number)
print(leafs)

print('-' * 50)


def return_x(stems):
    count = 0
    twodlist = []
    for x in stems:
        twodlist.append([x])
    for item in leafs:
        twodlist[count].append(item)
        count += 1
    return twodlist


b = return_x(stems)
print(b)
print('@' * 100)

'''file = open("giovanni", "w")
file.write("ciao")
file.close()
file = open("giovanni", "a")
file.write("buona sera")
file.close()
file = open("giovanni", "r")
file.close()
file = open("giovanni", "r")
print(file.read())'''

'''class HashTable2(object):

    def __init__(self, my_list):
        # Initiate our array with empty values.
        self.max = str(my_list[-1])[:-1]
        self.array = [None] * self.max

    def hash(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)
        if self.array[index] is not None:
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for kvp in self.array[index]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # If no breaks was hit in the for loop, it
                # means that no existing key was found,
                # so we can simply just add it to the end.
                self.array[index].append([key, value])
        else:
            # This index is empty. We should initiate
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does
            # then return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()'''

'''class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, ts):
        self.__size = 0
        self.__TABLE_SIZE = ts
        self.__table = [None] * ts
        self.__prime_size = self.__get_prime()

    def insert(self, key, value):
        """Insert a key value pair into the hash table
        """
        if self.__size == self.__TABLE_SIZE:
            raise RuntimeError("Table full!")

        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        self.__table[hash1] = HashEntry(key, value)
        self.__size += 1

    def remove(self, key):
        """Remove a key value pair from the hash table
        """
        if self.__size == 0:
            return

        hash1 = self.__hash1(key)
        hash2 = self.__hash2(hash1)

        while self.__table[hash1] is not None and self.__table[hash1].key != key:
            hash1 = (hash1 + hash2) % self.__TABLE_SIZE

        self.__table[hash1] = None
        self.__size -= 1

    def __get_prime(self):
        """Function to get a prime number less than table size
        """
        for i in range(self.__TABLE_SIZE - 1, 0, -1):
            fact = False
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    fact = True
                    break

            if not fact:
                return i

        return 3

    def __hash1(self, s):
        """Create hash value for a string s
        """
        hash_val = hash(s) % self.__TABLE_SIZE
        return hash_val if hash_val >= 0 else hash_val + self.__TABLE_SIZE

    def __hash2(self, h):
        """Create the second hash value based on the original hash

        The original is calculated using hash1
        """
        return self.__prime_size - h % self.__prime_size

    def __str__(self):
        s = ""
        for i in range(self.__TABLE_SIZE):
            if self.__table[i] is not None:
                print(self.__table[i].key, self.__table[i].value)

        return s
'''

'''def insertionSort_mod(values):
    k = 0
    n = len(values) - 1
    comparisons = 0
    while k + 1 <= n:
        i = k + 1
        curr_val = values[i]
        comparisons += 1
        while i > 0 and values[i - 1] > curr_val:
            values[i] = values[i - 1]
            i = i - 1
            comparisons += 1
        values[i] = curr_val
        k = k + 1
    return comparisons, values'''

# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
'''
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


n = len(numbers_list)
quickSort(numbers_list, 0, n - 1)
print("Sorted array is:")

print(numbers_list)
'''
''' def some(a, b):
    return a + b


result = some(4, 5)
print(result) '''

'''def stemleaf(result):
    d = OrderedDict((((str(v)[:-1], ' ')[v < 10], Counter()) for v in result))
    for s in ((str(v), ' ' + str(v))[v < 10] for v in result): d[s[:-1]][s[-1]] += 1
    m = max(len(s) for s in d)
    for k in d:
        print('%s%s | %s' % (' ' * (m - len(k)), k, ' '.join(sorted(d[k].elements()))))


stemleaf(sorted_number)'''

'''
# dynamic variable

# exec() method 1 
exec("x=12")

# dictionary method 2
variables = {}
for i in range(0, 3):
    key = input('please insert a key:')
    value = input('please insert a value:')
    variables[key] = value

print(variables)
'''
'''
def printdict(d):
    for key in d:
        print(key, "->", d[key])
  
  
hm = {0: 'first', 1: 'second', 2: 'third'}
printdict(hm)
print()
  
hm[3] = 'fourth'
printdict(hm)
print()
  
hm.popitem()
printdict(hm)'''


class HashTable:
  
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
  
    def create_buckets(self):
        return [[] for _ in range(self.size)]
  
    # Insert values into hash map
    def set_val(self, key, val):
        
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
  
    # Return searched value with specific key
    def get_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as 
            # the key being searched
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
  
    # Remove a value with specific key
    def delete_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
  
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  
  
hash_table = HashTable(50)
  
# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()
  
hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()
  
# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()
  
# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)