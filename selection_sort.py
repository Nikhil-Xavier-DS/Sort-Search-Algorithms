"""
Implementation of Selection Sort.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


def Selection_sort(arr):
    """Function to perform Selection sort in ascending order.

    TIME COMPLEXITY: Best:O(n^2), Average:O(n^2), Worst:O(n^2)
    SPACE COMPLEXITY: Worst: O(1)
    """

    for outer in range(len(arr)-1, 0, -1):
        max_position = 0
        for inner in range(1, outer+1):
            if arr[inner] > arr[max_position]:
                max_position = inner
        arr[max_position], arr[outer] = arr[outer], arr[max_position]
