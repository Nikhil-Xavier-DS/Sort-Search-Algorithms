"""
Implementation of Merge Sort.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


def merge_sort(arr):
    """Function to perform Merge sort in ascending order.

    TIME COMPLEXITY: Best:O(n ln(n)), Average:O(n ln(n)), Worst:O(n ln(n))
    SPACE COMPLEXITY: Worst: O(n)
    """

    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i, j, k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
            k = k + 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1
