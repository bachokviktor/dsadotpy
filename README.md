# dsadotpy

This repository contains my Python implementations of some data structures and algorithms.

## Example

See the [Installation](#installation) section for installation insctructions.

Use the module in your code

``` python
from dsadotpy.search import binary_search

arr = [...]
val = 3

index = binary_search(arr, val)
```

## What Is Implemented

**Sorting Algorithms:**

- Selection Sort: O(n^2)

**Searching Algorithms:**

- Binary Search: O(log n)

**Data Structures:**

- Linked Lists

## Installation

Remove the `dist` if already exists

``` bash
rm -r dist
```

Create a virtual environment

``` bash
python3 -m venv venv
```

Activate it

``` bash
source venv/bin/activate
```

Install dependencies

``` bash
pip install -r requirements.txt
```

Build the module

``` bash
python3 -m build
```

Install the `.wheel` file

``` bash
pip install dist/dsadotpy*.whl
```

## Testing

Install the package in editable mode

``` bash
pip install -e .
```

Run tests with pytest

``` bash
pytest -v
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
