from functools import reduce


def sort_between(num_list, start, end=None):
    if end is None:
        end = len(num_list)
    sorted_part = num_list[start: end]
    sorted_part.sort()
    for index in range(start, end):
        num_list[index] = sorted_part[index - start]


def next_permutation(num_list):
    """
    this function rearranges the list, to the next permutation in lexicographical order between start and end
    :param num_list: a list of different numbers
    :return: True if there is a next permutation. False if num_list is the maximal permutation, and it sorts it
    """
    first_change = len(num_list) - 2
    while num_list[first_change] > num_list[first_change + 1]:
        first_change -= 1
        if first_change == -1:
            num_list.sort()
            return False
    options = [num for num in num_list[first_change + 1:] if num > num_list[first_change]]
    next_first = num_list.index(min(options))
    num_list[first_change], num_list[next_first] = num_list[next_first], num_list[first_change]
    sort_between(num_list, first_change + 1)


list_num = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(1000000):
    next_permutation(list_num)

# The answer is 2783915460
print(reduce((lambda c1, c2: str(c1) + str(c2)), list_num))
