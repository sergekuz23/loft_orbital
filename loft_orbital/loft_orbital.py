import random
import multiprocessing
from typing import List, Dict

# Initializing 10 arrays of integers of size 10k with random values between 0 and 9

ten_random_arrays = [[random.randint(0, 9) for i in range(10 ** 4)] for i in range(10)]

# Bubble sorting function


def bubble_sort(lst: List[int]):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

# Counting a number of occurrences in a list


def count_number_of_occurrences(lst: List[int]) -> Dict[int, int]:
    return dict((x, lst.count(x)) for x in set(lst))

# Applying the lists to the functions


def go_over_list(lst: List[int]):
    print("Occurrences before sorting ", count_number_of_occurrences(lst))
    bubble_sort(lst)
    print("Occurrences after sorting ", count_number_of_occurrences(lst))


# Implementing multiprocessing to reduce the run time

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=len(ten_random_arrays))
    result1 = pool.map(go_over_list, ten_random_arrays)
