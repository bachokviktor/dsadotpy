import pytest

from dsadotpy import search


class TestBinarySearch:
    def test_binary_search(self):
        array = [1, 3, 6, 9, 14, 16, 22, 34, 77]
        value = 34

        result = search.binary_search(array, value)

        assert result == array.index(value)

    def test_string_array(self):
        array = ["a", "d", "n", "t", "w", "z"]
        value = "d"

        result = search.binary_search(array, value)

        assert result == array.index(value)

    def test_not_found(self):
        array = [1, 3, 6, 9, 14, 16, 22, 34, 77]
        value = 5

        result = search.binary_search(array, value)

        assert result == -1


class TestBreadthFirstSearch:
    def test_shortest_route(self):
        graph = {
            "London": ["Oxford", "Luton", "Cambridge", "Postmouth"],
            "Oxford": ["Cheltenham", "Northampton"],
            "Luton": ["Northampton"],
            "Cambridge": ["Northampton", "Peterborough"],
            "Postmouth": [],
            "Cheltenham": ["Birmingham"],
            "Northampton": ["Birmingham", "Leicester"],
            "Peterborough": ["Leicester"],
            "Leicester": ["Birmingham"],
            "Birmingham": [],
        }

        start = "London"

        shortest = ["London", "Oxford", "Cheltenham", "Birmingham"]

        route = search.bfs(
            graph, start, condition=lambda vert: vert == "Birmingham"
        )

        assert route == shortest

    def test_invalid_start(self):
        graph = {
            "London": ["Oxford", "Luton", "Cambridge"],
            "Oxford": ["Cheltenham", "Northampton"],
            "Luton": ["Northampton"],
            "Cambridge": ["Northampton"],
            "Cheltenham": [],
            "Northampton": [],
        }

        start = "Nonexistent"

        with pytest.raises(ValueError):
            search.bfs(
                graph, start, condition=lambda vert: vert == "Birmingham"
            )

    def test_not_found(self):
        graph = {
            "London": ["Oxford", "Luton", "Cambridge"],
            "Oxford": ["Cheltenham", "Northampton"],
            "Luton": ["Northampton"],
            "Cambridge": ["Northampton"],
            "Cheltenham": [],
            "Northampton": [],
        }

        start = "London"

        route = search.bfs(
            graph, start, condition=lambda vert: vert == "Birmingham"
        )

        assert route is None


class TestDijkstra:
    def test_shortest_route(self, weighted_graph):
        start = "London"

        shortest = ["London", "Luton", "Northampton", "Birmingham"]

        route = search.dijkstra(
            weighted_graph, start, condition=lambda vert: vert == "Birmingham"
        )

        assert route == shortest

    def test_invalid_start(self, weighted_graph):
        start = "Nonexistent"

        with pytest.raises(ValueError):
            search.dijkstra(
                weighted_graph,
                start,
                condition=lambda vert: vert == "Birmingham"
            )

    def test_not_found(self, weighted_graph):
        start = "London"

        route = search.dijkstra(
            weighted_graph, start, condition=lambda vert: vert == "Glasgow"
        )

        assert route is None
