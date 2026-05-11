import pytest


@pytest.fixture
def integer_array():
    initial_array = [5, 2, 3, 1, 4]
    sorted_array = [1, 2, 3, 4, 5]

    return (initial_array, sorted_array)


@pytest.fixture
def string_array():
    initial_array = ["d", "t", "z", "w", "a"]
    sorted_array = ["a", "d", "t", "w", "z"]

    return (initial_array, sorted_array)


@pytest.fixture
def weighted_graph():
    return {
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


@pytest.fixture
def negative_weight_graph():
    return {
        "A": {"B": 1},
        "B": {"C": 2, "E": -3},
        "C": {"D": 3, "H": -5},
        "D": {"A": 2, "G": 2},
        "E": {"F": 2},
        "F": {"G": 3},
        "G": {"E": 1, "H": 2},
        "H": {"E": 1},
    }


@pytest.fixture
def dependency_graph():
    return {
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
