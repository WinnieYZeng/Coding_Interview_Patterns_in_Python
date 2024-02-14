def two_pointers(array):
    left, right = 0, len(array) - 1
    while left <= right:
        left = left + 1
        right = right - 1
