"""
Implementation of Quick Sort.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


def Quick_sort(arr):
    """Function to perform Quick sort in ascending order.

    TIME COMPLEXITY: Best:O(n ln(n)), Average:O(n ln(n)), Worst: O(n^2)
    SPACE COMPLEXITY: Worst: O(ln(n))
    """

    _quick_sort(arr, 0, len(arr)-1)


def _quick_sort(arr, first, last):
    """Helper function to perform quick sort in ascending order.

    Called by quick_sort(). Calls helper function _pivot_func().
    """

    if first < last:
        splice_out = _pivot_func(arr, first, last)
        _quick_sort(arr, first, splice_out-1)
        _quick_sort(arr, splice_out+1, last)


def _pivot_func(arr, first, last):
    """Helper function to find splice out point of pivot element.

    Returns splice out index for pivot element. Called by _quick_sort().
    """

    pivot = arr[first]
    left_index = first + 1
    right_index = last
    done = False

    while not done:

        while left_index <= right_index and arr[left_index] <= pivot:
            left_index = left_index + 1

        while arr[right_index] >= pivot and right_index >= left_index:
            right_index = right_index - 1

        if left_index > right_index:
            done = True
        else:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]

    arr[right_index], arr[first] = arr[first], arr[right_index]
    return right_index
