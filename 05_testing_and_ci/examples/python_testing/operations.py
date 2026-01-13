"""
A set of mathematical operations.
"""

class MathOperations:

    def __init__(self, data):
        self._data = data

    def reorder_data(self):
        """
        Reorder data in ascending order
        """
        self._data.sort()

    def find_max(self):
        """
        Find maximum of all elements of a given list
        Parameters
        ----------
        data : list
            List of data. Elements are numbers

        Returns
        -------
        find_max : float
            Maximum of list
        """
        # Check that the input list has numbers
        for n in self._data:
            assert type(n) == int or type(n) == float

        max_num = self._data[0]  # Assume the first number is the maximum
        for n in self._data:
            if n > max_num:
                max_num = n

        return max_num

    def find_median(self):
        """
        Find median of all elements of a given list

        Parameters
        ----------
        data : list
            List of data. Elements are numbers

        Returns
        -------
        float : float
            Median of list
        """
        # Check that the input list has numbers
        for n in self._data:
            assert type(n) == int or type(n) == float

        # Sort the data to find the median
        sorted_data = sorted(self._data)
        n = len(sorted_data)
        
        # If odd number of elements, return the middle one
        if n % 2 == 1:
            return sorted_data[n // 2]
        # If even number of elements, return the average of the two middle ones
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2

    def find_mean(self):
        """
        Find mean of all elements of a given list

        Parameters
        ----------
        data : list
            List of data. Elements are numbers

        Returns
        -------
        float : float
            Mean of list
        """
        # Check that the input list has numbers
        for n in self._data:
            assert type(n) == int or type(n) == float

        total = sum(self._data)
        count = len(self._data)
        mean = total / count
        return mean


def main():
    data = [5, 3, 14, 27, 4, 9, 53]

    math_ops = MathOperations(data)

    maximum = math_ops.find_max()
    print("Maximum of {} is {}".format(data, maximum))

    median = math_ops.find_median()
    print("Median of {} is {}".format(data, median))

    mean = math_ops.find_mean()
    print("Mean of {} is {}".format(data, mean))


if __name__ == "__main__":
    main()
