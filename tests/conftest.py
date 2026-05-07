import pytest


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
