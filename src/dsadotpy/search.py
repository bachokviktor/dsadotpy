from collections import deque
from collections.abc import Sequence, Callable

from dsadotpy.protocols import Comparable


def binary_search[T: Comparable](array: Sequence[T], value: T) -> int:
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


if __name__ == "__main__":
    some_arr = [1, 3, 4, 7, 9, 12, 23, 24, 55]
    some_val = 24

    print("The index of", some_val, "is", binary_search(some_arr, some_val))

    str_arr = ["a", "d", "n", "t", "w", "z"]
    str_val = "d"
    print("The index of", str_val, "is", binary_search(str_arr, str_val))

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
