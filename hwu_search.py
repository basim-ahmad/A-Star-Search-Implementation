import heapq

class State:
    def isGoal(self):
        pass
    
    def getHeuristic(self):
        pass

class SearchOrder:
    def addToFringe(self, frontier, parent, children):
        pass
    
class ChildWithCost:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
        
    def __str__(self):
        return "ChildWithCost [node=" + str(self.node) + ", cost=" + str(self.cost) + "]"
    
class Node:
    def __init__(self, value):
        self.value = value
        self.children = set()
    
    def addChild(self, child, cost):
        if not (child in self.children):
            self.children.add(ChildWithCost(child, cost))
            return True
        else:
            return False
        
    def isGoal(self):
        return self.value.isGoal()
    
    def __str__(self):
        return "Node [value=" + str(self.value) + "]"
    
class FringeNode:
    def __init__(self, node, parent, cost):
        self.node = node
        self.parent = parent
        self.gValue = cost
        if (parent != None):
            self.gValue += parent.gValue
        
    def getFValue(self):
        return self.gValue + self.node.value.getHeuristic()
    
    def __str__(self):
        return "FringeNode [node=" + str(self.node) + ", parent=" + str(self.parent) + ", gValue=" + str(self.gValue) + "]"
    
class SearchProblem:
    def __init__(self, searchOrder):
        self.searchOrder = searchOrder
        
    def doSearch(self, root):
        fringe = list()
        fringe.append(FringeNode(root, None, 0))
        visitedStates = set()
        goalNode = None
        
        while (True):
            if (not(fringe)):
                break
            
            searchNode = fringe.pop(0)
            print("Current node: " + str(searchNode))
            
            if (searchNode.node in visitedStates):
                continue
            
            if (searchNode.node.isGoal()):
                goalNode = searchNode
                break
            
            self.searchOrder.addToFringe(fringe, searchNode, searchNode.node.children)
            visitedStates.add(searchNode.node)
        
        if (goalNode is None):
            print ("No goal found")
            return False
        else:
            print ("Found goal node: " + str(goalNode.node))
            print ("Cost: " + str(goalNode.gValue))
            print ("Nodes expanded: " + str(len(visitedStates)))
            print ("Path to root:")
            fNode = goalNode
            while (not(fNode is None)):
                print("- node:" + str(fNode.node.value))
                fNode = fNode.parent
            return True

# Implementation of the A* search algorithm

# Class representing the state of a grid in the A* search problem
class GridState(State):
    # Initialization of the GridState
    def __init__(self, grid, position, goal, cost=0, parent=None):
        self.grid = grid  # The grid representing the problem environment
        self.position = position  # The current position of the agent in the grid
        self.goal = goal  # The goal position in the grid
        self.cost = cost  # The cost to reach this state
        self.parent = parent  # The parent state in the path
    
    # Method to check if the current state is a goal state
    def isGoal(self):
        return self.position == self.goal
    
    # Method to calculate the heuristic value of the current state
    # Here we are using Manhattan distance as the heuristic
    def getHeuristic(self):
        x1, y1 = self.position
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)
    
    # Less than operator for comparing two GridState objects based on their f-values
    def __lt__(self, other):
        if isinstance(other, GridState):
            return self.cost + self.getHeuristic() < other.cost + other.getHeuristic()
        return False
    
    # String representation of the GridState
    def __str__(self):
        return f"GridState(position={self.position}, cost={self.cost}, heuristic={self.getHeuristic()})"

    # Equality operator for comparing two GridState objects based on their positions
    def __eq__(self, other):
        if isinstance(other, GridState):
            return self.position == other.position
        return False

    # Hash function for using GridState objects in sets or dictionaries
    def __hash__(self):
        return hash(self.position)

# Class representing the search order for A* search
class AStarSearchOrder(SearchOrder):
    # Method to add children to the fringe based on the A* search order
    def addToFringe(self, frontier, parent, children):
        for child in children:
            total_cost = parent.cost + child.cost
            priority = total_cost + child.node.getHeuristic()
            heapq.heappush(frontier, (priority, total_cost, child.node))

# Function to perform A* search on a grid
def a_star_search(grid, start_position, goal_position):
    start_state = GridState(grid, start_position, goal_position)  # Initializing the start state
    frontier = [(0 + start_state.getHeuristic(), 0, start_state)]  # Initializing the fringe with the start state
    explored = set()  # Set to store explored states
    order = AStarSearchOrder()  # Creating an instance of AStarSearchOrder
    while frontier:
        _, current_cost, current_state = heapq.heappop(frontier)  # Popping the state with the lowest f-value from the fringe
        if current_state.isGoal():
            path = []  # List to store the path from start to goal
            while current_state:
                path.append(current_state.position)  # Adding the current state's position to the path
                current_state = current_state.parent  # Moving to the parent state
            return path[::-1]  # Returning the reversed path (from start to goal)
        explored.add(current_state)  # Adding the current state to the set of explored states
        children = generate_children(grid, current_state)  # Generating the children of the current state
        order.addToFringe(frontier, current_state, [ChildWithCost(child, child.cost) for child in children if child not in explored])  # Adding the children to the fringe
    return None  # Returning None if no path is found

# Function to generate children of a state in the grid
def generate_children(grid, state):
    x, y = state.position  # Getting the current position
    children = []  # List to store the children states
    # Looping through possible moves (up, down, left, right)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy  # Calculating the new position after the move
        # Checking if the new position is within the grid and not a black square
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 'B':
            cost = 3 if grid[nx][ny] == 'Y' else 1  # Setting the cost based on the square's color
            child_state = GridState(grid, (nx, ny), state.goal, cost=cost, parent=state)  # Creating the child state
            children.append(child_state)  # Adding the child state to the list of children
    return children  # Returning the list of children
