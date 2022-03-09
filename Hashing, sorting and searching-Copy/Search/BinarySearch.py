class Search:

    def binary_search(self, a, t):
        """
        binary search method
        :param a: any list/array we want to search
        :param t: target number
        :return: the array with the middle value
        """
        l = 0  # assign to the variable l the the first index (0) of array
        r = len(a) - 1  # assign to the variable r the the last index (-1) of array

        steps = 0
        while l <= r:
            m = (l + r) // 2  # find the middle value of the array

            if a[m] < int(t):  # target assign l to middle of the array +1
                l = m + 1
                steps += 1
            elif a[m] > int(t):  # target assign r to middle of the array -1
                r = m - 1
                steps += 1
            else:

                return a[m]
