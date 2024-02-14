def two_pointers(array):
    left, right = 0, len(array) - 1
    while left <= right:
        left += 1
        right -= 1