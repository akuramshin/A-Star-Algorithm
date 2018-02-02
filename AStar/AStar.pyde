import random
import math

class node():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.parent = self
        self.f = 0
        self.cost = 1#random.randint(1, 10)
        self.wall = False
        self.g = float("inf")
        self.neighbors = []
        
        if random.randint(1, 10) < 3:
            self.wall = True;

    def getNeighbors(self, grid):
        if self.i > 0:
            self.neighbors.append(grid[self.i - 1][self.j])
        if self.i + 1 < gridSize:
            self.neighbors.append(grid[self.i + 1][self.j])
        if self.j > 0:
            self.neighbors.append(grid[self.i][self.j - 1])
        if self.j + 1 < gridSize:
            self.neighbors.append(grid[self.i][self.j + 1])

gridSize = 50
screenSize = 700
rectSize = screenSize / gridSize

grid = []
for n in range(gridSize):
    grid.append([])
    for h in range(gridSize):
        grid[n].append(node(n, h))

start = grid[0][0]
start.g = start.cost = 0
start.wall = False
end = grid[gridSize - 1][gridSize - 1]
end.wall = False
openSet = [start]
closedSet = []

def heuristic_cost_estimate(start, goal):
    return math.sqrt(abs(goal.i - start.i)^2 + abs(goal.j - start.j)^2)

def getLowest(list):
    lowest = list[0]
    for i in list:
        if i.f < lowest.f:
            lowest = i
    return lowest

def reconstructPath(current, path):
    if current.parent == current:
        return path
    path.append(current)
    return reconstructPath(current.parent, path)

def setup():
    size(screenSize, screenSize)
    #frameRate(30)

    
def draw():
    background(255, 255, 255)
    for n in range(gridSize):
        for h in range(gridSize):
            fill(255, 255, 255)
            if grid[n][h].wall:
                fill(0, 0, 0)
            rect(n * rectSize, h * rectSize, rectSize, rectSize)
            
    if len(openSet) > 0:
        current = getLowest(openSet)
        current.getNeighbors(grid)
        
        path = reconstructPath(current, [start])
        for i in path:
            fill(0, 255, 0)
            rect(i.i * rectSize, i.j * rectSize, rectSize, rectSize)

        if current == end:
            noLoop()
            return 
        openSet.remove(current)
        closedSet.append(current)

        for neighbor in current.neighbors:
            if neighbor in closedSet or neighbor.wall:
                continue
            if neighbor not in openSet:
                openSet.append(neighbor)

            tentative_gScore = current.g + neighbor.cost
            if tentative_gScore >= neighbor.g:
                continue

            neighbor.parent = current
            neighbor.g = tentative_gScore
            neighbor.f = neighbor.g + heuristic_cost_estimate(neighbor, end)