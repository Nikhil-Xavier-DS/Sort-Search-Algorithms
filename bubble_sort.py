"""
Implementation of Bubble Sort.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


def Bubble_sort(arr):
    """Function to perform Bubble sort in ascending order.

    TIME COMPLEXITY: Best:O(n), Average:O(n^2), Worst:O(n^2)
    SPACE COMPLEXITY: Worst: O(1)
    """

    for outer in range(len(arr)-1, 0, -1):
        for inner in range(outer):
            if arr[inner] > arr[inner+1]:
                arr[inner], arr[inner+1] = arr[inner+1], arr[inner]
