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


class TestBellmanFord:
    def test_shortest_route(self, negative_weight_graph):
        start = "A"

        shortest = ["A", "B", "E", "F", "G"]

        route = graphs.bellman_ford(
            negative_weight_graph, start, lambda vert: vert == "G"
        )

        assert route == shortest

    def test_invalid_start(self, negative_weight_graph):
        start = "Nonexistent"

        with pytest.raises(ValueError):
            graphs.bellman_ford(
                negative_weight_graph,
                start,
                condition=lambda vert: vert == "G"
            )

    def test_not_found(self, negative_weight_graph):
        start = "A"

        route = graphs.bellman_ford(
            negative_weight_graph, start, lambda vert: vert == "X"
        )

        assert route is None

    def test_negative_cycle(self):
        graph = {
            "A": {"B": 1},
            "B": {"C": -2},
            "C": {"A": -3},
        }

        start = "A"

        with pytest.raises(ValueError):
            graphs.bellman_ford(
                graph,
                start,
                condition=lambda vert: vert == "C"
            )


class TestDepthFirstSearch:
    def test_topological_sort(self, dependency_graph):
        start = "emacs"

        sorted_graph = [
            "GMP", "MPC", "MPFR",
            "gcc", "glibc", "libxcb",
            "xorgproto", "libx11",
            "libtree-sitter", "emacs"
        ]

        result = graphs.dfs(dependency_graph, start)

        assert result == sorted_graph

    def test_invalid_start(self, dependency_graph):
        start = "vim"

        with pytest.raises(ValueError):
            graphs.dfs(dependency_graph, start)
