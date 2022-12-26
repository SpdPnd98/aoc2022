from collections import deque

def main():
    partTwo()

def partOne():
    ultimateMaze = parseMaze()
    # print(mazeString(ultimateMaze.generateState(1), (1, 0)))
    queue = deque([(0, tuple(startingPoint))])
    visited = set()


    while queue:
        currentTime, currentLocation = queue.popleft()
        nextMaze = ultimateMaze.generateState(currentTime + 1)
        validPos = generateValidPos(currentLocation, nextMaze)
        # print(nextMaze)
        # print("Current Time: %d" % currentTime)
        # print(mazeString(ultimateMaze.generateState(currentTime), currentLocation))
        # print()
        if not validPos:
            continue
        else:
            for pos in validPos:
                if pos == endingPoint:
                    print("Found exit at time: %d" %(currentTime + 1))
                    return
                elif (currentTime, pos) in visited or not nextMaze[pos[1]][pos[0]]:
                    continue # no need to explore again as it is invalid or seen
                else:
                    queue.append((currentTime + 1, pos))
                    visited.add((currentTime, pos))


def generateValidPos(pos, maze):
    x, y = pos
    validLocs = []
    for pos in [(x-1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x, y)]:
        if pos == endingPoint or pos == startingPoint or within(pos[0], pos[1]) and maze[pos[1]][pos[0]]:
            validLocs.append(pos)
    return validLocs

def mazeString(maze, currentPos):
    print(maze)
    total = ""
    currentX, currentY = currentPos
    for y in range(0, len(maze)):
        rowStr = ""
        for x in range(0, len(maze[y])):
            rowStr += "#" if not maze[y][x] else "S" if x == currentX and y == currentY else "."
        total += rowStr + "\n"
    return total

def noBlocks(x, y, maze):
    return maze[y][x]

def partTwo():
    ultimateMaze = parseMaze()
    # print(mazeString(ultimateMaze.generateState(1), (1, 0)))
    queue = deque([(0, tuple(startingPoint))])
    visited = set()
    exitState = None

    while queue:
        currentTime, currentLocation = queue.popleft()
        nextMaze = ultimateMaze.generateState(currentTime + 1)
        validPos = generateValidPos(currentLocation, nextMaze)
        exitState = None
        # print(nextMaze)
        # print("Current Time: %d" % currentTime)
        # print(mazeString(ultimateMaze.generateState(currentTime), currentLocation))
        # print()
        if not validPos:
            continue
        else:
            for pos in validPos:
                if pos == endingPoint:
                    print("Found exit at time: %d" %(currentTime + 1))
                    exitState = (currentTime + 1, pos)
                    break
                elif (currentTime, pos) in visited or not nextMaze[pos[1]][pos[0]]:
                    continue # no need to explore again as it is invalid or seen
                else:
                    queue.append((currentTime + 1, pos))
                    visited.add((currentTime, pos))
        if exitState != None:
            break
    queue = deque([exitState])
    visited = set()
    exitState = None

    while queue:
        currentTime, currentLocation = queue.popleft()
        nextMaze = ultimateMaze.generateState(currentTime + 1)
        validPos = generateValidPos(currentLocation, nextMaze)
        # print(nextMaze)
        # print("Current Time: %d" % currentTime)
        # print(mazeString(ultimateMaze.generateState(currentTime), currentLocation))
        # print()
        if not validPos:
            continue
        else:
            for pos in validPos:
                if pos == startingPoint:
                    print("Found start at time: %d" %(currentTime + 1))
                    exitState = (currentTime + 1, pos)
                    break
                elif (currentTime, pos) in visited or not nextMaze[pos[1]][pos[0]]:
                    continue # no need to explore again as it is invalid or seen
                else:
                    queue.append((currentTime + 1, pos))
                    visited.add((currentTime, pos))
        if exitState != None:
            break
    
    queue = deque([exitState])
    visited = set()
    exitState = None

    while queue:
        currentTime, currentLocation = queue.popleft()
        nextMaze = ultimateMaze.generateState(currentTime + 1)
        validPos = generateValidPos(currentLocation, nextMaze)
        exitState = None
        # print(nextMaze)
        # print("Current Time: %d" % currentTime)
        # print(mazeString(ultimateMaze.generateState(currentTime), currentLocation))
        # print()
        if not validPos:
            continue
        else:
            for pos in validPos:
                if pos == endingPoint:
                    print("Found exit at time: %d" %(currentTime + 1))
                    exitState = (currentTime + 1, pos)
                    break
                elif (currentTime, pos) in visited or not nextMaze[pos[1]][pos[0]]:
                    continue # no need to explore again as it is invalid or seen
                else:
                    queue.append((currentTime + 1, pos))
                    visited.add((currentTime, pos))
        if exitState != None:
            break


def parseMaze():
    global perimeter, startingPoint, endingPoint
    with open("input.txt") as f:
        blizzards = {
            ">": [],
            "<": [],
            "^": [],
            "v": [],
            "#": [],
        }
        for y, line in enumerate(f.readlines()):
            if perimeter is None:
                perimeter = [len(line)- 1, 0]
            perimeter[1] += 1
            for x, char in enumerate(line.strip()):
                if char == ".":
                    continue
                elif char == "#" or char == ">" or char == "<" or char == "^" or char == "v":
                    blizzards[char].append((x, y))
                else:
                    print("Invalid char detected")
        startingPoint = (1, 0)
        endingPoint = (perimeter[0] - 2, perimeter[1] - 1)
        print(perimeter, startingPoint, endingPoint)
        return UltimateMaze(blizzards)

perimeter = None
startingPoint = None
endingPoint = None

def within(x, y):
    if x < 1 or x >= perimeter[0] - 1 or y < 1 or y >= perimeter[1] - 1:
        return False
    return True

blizzardFunction = {
    ">": lambda x, y: (x + 1, y) if within(x + 1, y) else (1, y),
    "<": lambda x, y: (x - 1, y) if within(x - 1, y) else (perimeter[0]-2, y),
    "^": lambda x, y: (x, y - 1) if within(x, y - 1) else (x, perimeter[1]-2),
    "v": lambda x, y: (x, y + 1) if within(x, y + 1) else (x, 1),
}

class UltimateMaze:
    def __init__(self, blizzards):
        self.blizzards = blizzards
        self.counter = 0
        self.allStates = {}

        blizzardSet = set()
        for direction in self.blizzards:
            for coordinates in self.blizzards[direction]:
                blizzardSet.add(coordinates)
        
        obstacleMap = []
        for y in range(0, perimeter[1]):
            newRow = []
            for x in range(0, perimeter[0]):
                newRow.append(not (x, y) in blizzardSet)
            obstacleMap.append(newRow)
        self.allStates[0] = obstacleMap
    
    def generateState(self, minute):
        if minute not in self.allStates:
            newBlizzards = {}
            blizzardSet = set()
            for direction in self.blizzards:
                newBlizzard = []
                for coordinates in self.blizzards[direction]:
                    if direction == "#":
                        blizzardSet.add(coordinates)
                        newBlizzard.append(coordinates)
                    else:
                        newCoordinate = blizzardFunction[direction](coordinates[0], coordinates[1])
                        newBlizzard.append(newCoordinate)
                        blizzardSet.add(newCoordinate)
                newBlizzards[direction] = newBlizzard
            
            self.blizzards = newBlizzards
            obstacleMap = []
            for y in range(0, perimeter[1]):
                newRow = []
                for x in range(0, perimeter[0]):
                    newRow.append(not (x, y) in blizzardSet)
                obstacleMap.append(newRow)
            self.allStates[minute] = obstacleMap
        return self.allStates[minute]


if __name__ == "__main__":
    main()