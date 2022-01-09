"""
A set of mathematical operations.
"""


def find_max(array):
    max_num = array[0]  # Assume the first number is the maximum
    for n in array:
        if n > max_num:
            max_num = n

    return max_num


def find_average(array):
    sum_n = 0
    for n in array:
        sum_n += n

    return sum_n / len(array)


def main():
    data = [5, 3, 14, 27, 4, 9]

    for n in data:
        assert type(n) == int or type(n) == float

    maximum = find_max(data)
    print("Maximum = {}".format(maximum))

    average = find_average(data)
    print("Average = {}".format(average))


if __name__ == "__main__":
    main()
