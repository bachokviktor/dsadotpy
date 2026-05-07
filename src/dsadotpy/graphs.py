from collections import deque
from collections.abc import Callable


def _reconstruct_path[T](checked: dict[T, T | None], final: T) -> list[T]:
    path = []

    current: T | None = final
    while current:
        path.append(current)
        current = checked[current]

    return path[::-1]


def bfs[T](
        graph: dict[T, list[T]], start: T, condition: Callable[[T], bool]
) -> list[T] | None:
    """
    Searches for the closest vertex inside a graph for
    which the condition is true using the breadth-first search.

    Using a condition insted of a name of the searched vertex allows
    to use this function for a wider range of problems.

    Args:
        graph: Graph represented as an adjacency list.
        start: The starting vertex.
        condition: Function that will accept one argument (vertex) and
            return True or False depending on some condition.

    Returns:
        Shortest path represented as a sequence
        of vertices, or None if not found.
    """
    start_node = graph.get(start)
    if start_node is None:
        raise ValueError(f"{start} is not in the graph.")

    queue = deque([start])
    checked: dict[T, T | None] = {start: None}

    while queue:
        vertex = queue.popleft()

        if condition(vertex):
            return _reconstruct_path(checked, vertex)

        for vert in graph[vertex]:
            if vert not in checked:
                checked[vert] = vertex
                queue.append(vert)

    return None


def dijkstra[T](
        graph: dict[T, dict[T, float]],
        start: T,
        condition: Callable[[T], bool]
) -> list[T] | None:
    """
    Searches for the closest vertex inside a weighted graph for
    which the condition is true using the Dijkstra's algorithm.

    Using a condition insted of a name of the searched vertex allows
    to use this function for a wider range of problems.

    Args:
        graph: Graph represented as an adjacency list.
        start: The starting vertex.
        condition: Function that will accept one argument (vertex) and
            return True or False depending on some condition.

    Returns:
        Shortest path represented as a sequence
        of vertices, or None if not found.
    """
    start_node = graph.get(start)
    if start_node is None:
        raise ValueError(f"{start} is not in the graph.")

    parents: dict[T, T | None] = {start: None}
    checked: list[T] = []
    costs: dict[T, float] = {v: float("inf") for v in graph}
    costs[start] = 0

    current: T | None = start
    while current is not None:
        weight = costs[current]

        if condition(current):
            return _reconstruct_path(parents, current)

        for v, w in graph[current].items():
            if weight+w < costs[v]:
                costs[v] = weight+w
                parents[v] = current

        checked.append(current)

        cheapest_w: float = float("inf")
        cheapest_v: T | None = None
        for v, w in costs.items():
            if (w < cheapest_w) and v not in checked:
                cheapest_w = w
                cheapest_v = v

        current = cheapest_v

    return None


def _dfs_recursion[T](
        graph: dict[T, list[T]], node: T, visited: list[T]
) -> None:
    for dependency in graph[node]:
        if dependency not in visited:
            _dfs_recursion(graph, dependency, visited)

    visited.append(node)


def dfs[T](graph: dict[T, list[T]], start: T) -> list[T]:
    """
    Topologically sorts a directed acyclic dependency graph
    using the Depth-First Search algorithm.

    Args:
        graph: Graph represented as an adjacency list.
        start: The starting vertex. It has to be in-degree zero (with
            no incoming edges).

    Returns:
        Topologically sorted list of nodes.
    """
    node = graph.get(start)
    if node is None:
        raise ValueError(f"{start} is not in the graph.")

    visited: list[T] = []

    _dfs_recursion(graph, start, visited)

    return visited


if __name__ == "__main__":
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

    route = bfs(graph, start, condition=lambda vert: vert == "Birmingham")

    print(route)

    wgraph: dict[str, dict[str, float]] = {
        "London": {
            "Oxford": 96,
            "Luton": 55,
            "Cambridge": 93,
            "Postmouth": 120,
        },
        "Oxford": {
            "Cheltenham": 70,
            "Northampton": 80,
        },
        "Luton": {
            "Northampton": 58,
        },
        "Cambridge": {
            "Northampton": 91,
            "Peterborough": 70,
        },
        "Postmouth": {},
        "Cheltenham": {
            "Birmingham": 96,
        },
        "Northampton": {
            "Birmingham": 87,
            "Leicester": 73,
        },
        "Peterborough": {
            "Leicester": 66,
        },
        "Leicester": {
            "Birmingham": 71,
        },
        "Birmingham": {},
    }

    start = "London"

    route = dijkstra(
        wgraph, start, condition=lambda vert: vert == "Birmingham"
    )

    print(route)

    dgraph = {
        "emacs": ["gcc", "libx11", "libtree-sitter"],
        "gcc": ["GMP", "MPC", "MPFR"],
        "libx11": ["glibc", "libxcb", "xorgproto"],
        "libtree-sitter": ["glibc"],
        "GMP": [],
        "MPC": [],
        "MPFR": [],
        "libxcb": [],
        "xorgproto": [],
        "glibc": [],
    }

    start = "emacs"

    dsorted = dfs(dgraph, start)

    print(dsorted)
