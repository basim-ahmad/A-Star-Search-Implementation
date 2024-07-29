# A* Search Implementation

## Overview
This repository contains an implementation of the A* search algorithm, as well as additional search strategies like Breadth-First Search (BFS) and Depth-First Search (DFS). The project includes Python scripts for defining the search problem and running the A* search on grid problems.

## Files

- `hwu_search.py`: Contains the main implementation of the A* search algorithm and supporting classes.
- `run.py`: Demonstrates the usage of the search implementation with BFS, DFS, and A* search on sample grid problems.

## A* Search Algorithm

The A* search algorithm is implemented using the following classes:

- `State`: Represents the state in the search problem.
- `SearchOrder`: Defines the order in which nodes are added to the fringe.
- `ChildWithCost`: Represents a child node with an associated cost.
- `Node`: Represents a node in the search tree.
- `FringeNode`: Represents a node in the fringe with a cost.
- `SearchProblem`: Manages the search process.
- `GridState`: Represents the state of a grid in the A* search problem.
- `AStarSearchOrder`: Defines the order for the A* search strategy.

## How to Use

### Running the Search

To run the search on the sample grids, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/basim-ahmad/A-Star-Search-Implementation.git
    cd A-Star-Search-Implementation
    ```

2. Make sure you have Python 3.x installed. You can check your Python version by running:
    ```sh
    python --version
    ```

3. Execute the `run.py` script:
    ```sh
    python run.py
    ```

The script will output the path found by the search algorithm and the cost associated with it, as well as print the grid with the path marked.

### Sample Grids

The `run.py` file includes sample grids for testing the search algorithms:

```python
grid1 = [
    ['S', 'Y', 'W', 'W', 'W', 'W'],
    ['W', 'Y', 'B', 'W', 'Y', 'W'],
    ['W', 'W', 'Y', 'B', 'Y', 'W'],
    ['W', 'W', 'W', 'B', 'G', 'W']
]

grid2 = [
    ['S', 'W', 'W', 'W', 'W'],
    ['Y', 'B', 'B', 'B', 'Y'],
    ['W', 'W', 'B', 'W', 'W'],
    ['B', 'W', 'Y', 'W', 'Y'],
    ['W', 'W', 'W', 'W', 'G']
]
```
## Running A* Search

To run the A* search on the sample grids, the script finds the start and goal positions, then performs the search to find the optimal path.

# Dependencies

This project requires Python 3.x. No additional external libraries are needed.

# License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
