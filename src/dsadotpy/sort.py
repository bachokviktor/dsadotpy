from dsadotpy.protocols import Comparable


def selection_sort[T: Comparable](array: list[T]) -> list[T]:
    """
    Sorts an array using selection sort.

    Args:
        array: The initial array.

    Returns:
        The new sorted array.
    """
    for i in range(len(array)):
        smallest_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j

        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array


def _merge[T: Comparable](left: list[T], right: list[T]) -> list[T]:
    sorted_array: list[T] = []

    l_index = 0
    l_len = len(left)

    r_index = 0
    r_len = len(right)

    while l_index < l_len and r_index < r_len:
        if left[l_index] < right[r_index]:
            sorted_array.append(left[l_index])
            l_index += 1
        else:
            sorted_array.append(right[r_index])
            r_index += 1

    sorted_array += left[l_index:]
    sorted_array += right[r_index:]

    return sorted_array


def merge_sort[T: Comparable](array: list[T]) -> list[T]:
    """
    Sorts an array using the merge sort algorithm.

    Args:
        array: The initial array.

    Returns:
        The new sorted array.
    """
    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return _merge(left, right)


def quicksort[T: Comparable](array: list[T]) -> list[T]:
    """
    Sorts an array using the quicksort algorithm.

    Args:
        array: The initial array.

    Returns:
        The new sorted array.
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    print("Selection Sort")

    arr = [1, 6, 2, 9, 44, 11]

    print(arr)

    new_arr = selection_sort(arr)

    print(new_arr)

    arr_str = ["n", "d", "z", "a", "w", "t"]

    print(arr_str)

    new_arr_str = selection_sort(arr_str)

    print(new_arr_str)

    print("\nQuicksort")

    arr = [1, 6, 2, 9, 44, 11]

    print(arr)

    new_arr = quicksort(arr)

    print(new_arr)

    arr_str = ["n", "d", "z", "a", "w", "t"]

    print(arr_str)

    new_arr_str = quicksort(arr_str)

    print(new_arr_str)

    print("\nMerge sort")

    arr = [1, 6, 2, 9, 44, 11]

    print(arr)

    new_arr = merge_sort(arr)

    print(new_arr)

    arr_str = ["n", "d", "z", "a", "w", "t"]

    print(arr_str)

    new_arr_str = merge_sort(arr_str)

    print(new_arr_str)
