from dsadotpy import sort


class TestSelectionSort:
    def test_integer_array(self):
        initial_array = [5, 2, 3, 1, 4]
        sorted_array = [1, 2, 3, 4, 5]

        result = sort.selection_sort(initial_array)

        assert result == sorted_array

    def test_string_array(self):
        initial_array = ["d", "t", "z", "w", "a"]
        sorted_array = ["a", "d", "t", "w", "z"]

        result = sort.selection_sort(initial_array)

        assert result == sorted_array


class TestQuicksort:
    def test_integer_array(self):
        initial_array = [5, 2, 3, 1, 4]
        sorted_array = [1, 2, 3, 4, 5]

        result = sort.quicksort(initial_array)

        assert result == sorted_array

    def test_string_array(self):
        initial_array = ["d", "t", "z", "w", "a"]
        sorted_array = ["a", "d", "t", "w", "z"]

        result = sort.quicksort(initial_array)

        assert result == sorted_array
