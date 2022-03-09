class HashTable:

    def __init__(self, sorted_number):
        """
        create hash table with multiple methods
        :param sorted_number:
        """
        self.m = str(sorted_number[-1])[:-1]

        self.arr = ([None for i in range(int(self.m) + 1)])  # creating an array of None value

    def get_hash_key(self, number):
        h = number // 10  # getting the hash key and return it
        return h

    def add(self, value):
        h = self.get_hash_key(value)

        if self.arr[h] is None:  # if the array is None add a new value to the list

            self.arr[h] = list([int(str(value)) % 10])
            return True
        else:
            self.arr[h].append(int(str(value)) % 10)  # append values to the list if list already contain other value
            return True

    def print(self):  # print the steam and leaves for our tree

        for value in self.arr:  # loop true the value we have
            if value is not None:
                stem = self.arr.index(value)
                print(f"{stem}", end="|")  # printing stem
                for leaf in value:
                    print(f"{leaf}", end=",")  # printing leaves
                print("")
