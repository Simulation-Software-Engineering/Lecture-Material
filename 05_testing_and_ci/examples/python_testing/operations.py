"""
A set of mathematical operations.
"""


def find_max(data):
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
    for n in data:
        assert type(n) == int or type(n) == float

    max_num = data[0]  # Assume the first number is the maximum
    for n in data:
        if n > max_num:
            max_num = n

    return max_num


def find_mean(data):
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
    for n in data:
        assert type(n) == int or type(n) == float

    return sum(data) / len(data)


def main():
    data = [5, 3, 14, 27, 4, 9]

    maximum = find_max(data)
    print("Maximum = {}".format(maximum))

    mean = find_mean(data)
    print("Average = {}".format(mean))


if __name__ == "__main__":
    main()
