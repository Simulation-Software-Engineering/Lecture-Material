"""
A set of mathematical operations.
"""


def find_max(array):
    # Check that the input list has numbers
    for n in array:
        assert type(n) == int or type(n) == float

    max_num = array[0]  # Assume the first number is the maximum
    for n in array:
        if n > max_num:
            max_num = n

    return max_num


def find_mean(array):
    # Check that the input list has numbers
    for n in array:
        assert type(n) == int or type(n) == float

    return sum(array) / len(array)


def main():
    data = [5, 3, 14, 27, 4, 9]

    maximum = find_max(data)
    print("Maximum = {}".format(maximum))

    mean = find_mean(data)
    print("Average = {}".format(mean))


if __name__ == "__main__":
    main()
