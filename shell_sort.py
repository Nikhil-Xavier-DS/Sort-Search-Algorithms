"""
Implementation of Shell Sort.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


def shell_sort(arr):
    """Function to perform Shell sort in ascending order.

    TIME COMPLEXITY: Best:O(n ln(n)), Average:O(n ln(n)^2), Worst:O(n ln(n)^2)
    SPACE COMPLEXITY: Worst: O(1)
    """

    sub_count = len(arr)//2
    while sub_count > 0:
        for start in range(sub_count):
            gap_insertion_sort(arr, start, sub_count)
        sub_count = sub_count//2


def gap_insertion_sort(array, start, gap):
    for i in range(start+gap, len(array), gap):
        current_value = array[i]
        current_position = i
        while current_position >= gap and array[current_position-gap] > current_value:
            array[current_position] = array[current_position-gap]
            current_position = current_position - gap
        array[current_position] = current_value
