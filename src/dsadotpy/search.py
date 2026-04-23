from collections.abc import Sequence


def binary_search(array: Sequence[int], value: int) -> int:
    """
    Searches for a value in a sorted array using binary search.

    Args:
        array: A sorted arrays of elements.
        value: The searched value.

    Returns:
        The index of the searched value or -1 if not found.
    """
    lowest = 0
    highest = len(array) - 1

    while lowest <= highest:
        middle = (lowest + highest) // 2

        if array[middle] == value:
            return middle
        if array[middle] > value:
            highest = middle - 1
        else:
            lowest = middle + 1

    return -1


if __name__ == "__main__":
    some_arr = [1, 3, 4, 7, 9, 12, 23, 24, 55]
    some_val = 24

    print("The index of", some_val, "is", binary_search(some_arr, some_val))
