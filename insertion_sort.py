"""
Implementation of Insertion Sort.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


def Insertion_sort(arr):
    """Function to perform Insertion sort in ascending order.

    TIME COMPLEXITY: Best:O(n), Average:O(n^2), Worst:O(n^2)
    SPACE COMPLEXITY: Worst: O(1)
    """

    for outer in range(1, len(arr)):
        current_value = arr[outer]
        current_position = outer
        while current_position > 0 and arr[current_position-1] > current_value:
            arr[current_position] = arr[current_position-1]
            current_position = current_position - 1
        arr[current_position] = current_value

