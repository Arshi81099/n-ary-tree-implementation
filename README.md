# N-ary Tree Implementation in Python

This repository contains a Python implementation of an N-ary tree data structure, along with functions to create the tree, perform postorder and level order traversals, and print the tree structure.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

An N-ary tree is a tree data structure where each node can have up to N children. This implementation allows for dynamic creation of the tree from a list of values and provides various traversal methods.

## Features

- Create an N-ary tree from a list of values.
- Print the tree structure in a readable format.
- Perform postorder traversal and level order traversal.
- Support for `None` values to represent null children.

## Installation

To run the code, make sure you have Python 3 installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Clone the repository to your local machine using:

```bash
git clone https://github.com/Arshi81099/n-ary-tree-implementation.git
```

Navigate into the project directory:

```bash
cd n-ary-tree-implementation
```

## Usage

1. Open the `main.py` file.
2. Modify the `values` list to create your desired N-ary tree.
3. Run the script:

```bash
python3 main.py
```

## Example

Here's an example of how to use the implementation:

```python
input_values = input("Enter the values for the N-ary tree (use 'None' for nulls, separated by spaces): ")
values = [int(x) if x != 'None' else None for x in input_values.split()]
solution = Solution()
root = solution.createTree(values)

print("Tree structure:")
solution.print_tree(root)
print("Postorder traversal:", solution.postorder(root))
print("Level order traversal:", solution.levelOrder(root))
```

### Input

For the above example, you can use the input:
```
1 None 2 3 4 5 None None 6 7 None 8 None 9 10 None None 11 None 12 None 13 None None 14
```

### Output

```
Tree structure:
1
  2
  3
    6
    7
      11
        14
  4
    8
      12
  5
    9
      13
    10

Postorder traversal: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
Level order traversal: [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.


