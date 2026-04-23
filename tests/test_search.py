from dsadotpy import search


class TestBinarySearch:
    def test_binary_search(self):
        array = [1, 3, 6, 9, 14, 16, 22, 34, 77]
        value = 34

        result = search.binary_search(array, value)

        assert result == array.index(value)

    def test_binary_search_not_found(self):
        array = [1, 3, 6, 9, 14, 16, 22, 34, 77]
        value = 5

        result = search.binary_search(array, value)

        assert result == -1
