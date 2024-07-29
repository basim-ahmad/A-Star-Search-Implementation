import hwu_search

class BreadthFirstSearchOrder(hwu_search.SearchOrder):
    def addToFringe(self, frontier, parent, children):
        for child in children:
            frontier.append(hwu_search.FringeNode(child.node, parent, child.cost))

class DepthFirstSearchOrder(hwu_search.SearchOrder):
    def addToFringe(self, frontier, parent, children):
        for child in children:
            frontier.insert(0, hwu_search.FringeNode(child.node, parent, child.cost))

class IntState(hwu_search.State):
    def __init__(self, value, goal=False):
        self.value = value
        self.goal = goal 
    
    def isGoal(self):
        return self.goal 
    
    def getHeuristic(self):
        return 0
    
    def __str__(self):
        return "IntegerState [value=" + str(self.value) + ", goal=" + str(self.goal) + "]"
    
def addChild(value, goal, parent):
    child = hwu_search.Node(IntState(value, goal))
    parent.addChild(child, 1)
    return child

root = hwu_search.Node(IntState(0))
goal = hwu_search.Node(IntState(5, True))
child = addChild(1, False, root)
child = addChild(2, False, child)
child = addChild(3, False, child)
addChild(4, False, child)
root.addChild(goal, 1)

order = DepthFirstSearchOrder()
problem = hwu_search.SearchProblem(order)
problem.doSearch(root)

# A* Search on Grid Problems
# ---------------------------

# Grids for the A* search problems
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

# Function to find the start and goal positions in a grid
def find_positions(grid):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'G':
                goal = (x, y)
    return start, goal

# Function to print the grid
def print_grid(grid, path):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if (x, y) in path:
                print('P', end=' ')
            else:
                print(cell, end=' ')
        print()

# Function to run A* search on a grid
def run_a_star(grid):
    start, goal = find_positions(grid)
    path = hwu_search.a_star_search(grid, start, goal)
    if path:
        print('Path:', path)
        print('Cost:', len(path) - 1)
        print_grid(grid, path)
    else:
        print('No path found')
    print('\n')

print('Grid 1:')
run_a_star(grid1)

print('Grid 2:')
run_a_star(grid2)
