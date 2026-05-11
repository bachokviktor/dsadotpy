from dsadotpy import sort


class TestSelectionSort:
    def test_integer_array(self, integer_array):
        initial_array, sorted_array = integer_array

        result = sort.selection_sort(initial_array)

        assert result == sorted_array

    def test_string_array(self, string_array):
        initial_array, sorted_array = string_array

        result = sort.selection_sort(initial_array)

        assert result == sorted_array


class TestMergeSort:
    def test_integer_array(self, integer_array):
        initial_array, sorted_array = integer_array

        result = sort.merge_sort(initial_array)

        assert result == sorted_array

    def test_string_array(self, string_array):
        initial_array, sorted_array = string_array

        result = sort.merge_sort(initial_array)

        assert result == sorted_array


class TestQuicksort:
    def test_integer_array(self, integer_array):
        initial_array, sorted_array = integer_array

        result = sort.quicksort(initial_array)

        assert result == sorted_array

    def test_string_array(self, string_array):
        initial_array, sorted_array = string_array

        result = sort.quicksort(initial_array)

        assert result == sorted_array
