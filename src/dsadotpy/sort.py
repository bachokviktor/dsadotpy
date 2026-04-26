from typing import Any, TypeVar, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


def selection_sort(array: list[T]) -> list[T]:
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


if __name__ == "__main__":
    arr = [1, 6, 2, 9, 44, 11]

    print(arr)

    new_arr = selection_sort(arr)

    print(new_arr)

    arr_str = ["n", "d", "z", "a", "w", "t"]

    print(arr_str)

    new_arr_str = selection_sort(arr_str)

    print(new_arr_str)
