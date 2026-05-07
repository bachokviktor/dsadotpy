import pytest

from dsadotpy import graphs


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

        route = graphs.bfs(
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
            graphs.bfs(
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

        route = graphs.bfs(
            graph, start, condition=lambda vert: vert == "Birmingham"
        )

        assert route is None


class TestDijkstra:
    def test_shortest_route(self, weighted_graph):
        start = "London"

        shortest = ["London", "Luton", "Northampton", "Birmingham"]

        route = graphs.dijkstra(
            weighted_graph, start, condition=lambda vert: vert == "Birmingham"
        )

        assert route == shortest

    def test_invalid_start(self, weighted_graph):
        start = "Nonexistent"

        with pytest.raises(ValueError):
            graphs.dijkstra(
                weighted_graph,
                start,
                condition=lambda vert: vert == "Birmingham"
            )

    def test_not_found(self, weighted_graph):
        start = "London"

        route = graphs.dijkstra(
            weighted_graph, start, condition=lambda vert: vert == "Glasgow"
        )

        assert route is None
