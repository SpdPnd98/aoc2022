from collections import deque

def main():
    partTwo()

def partOne():
    maze, startPos, endPos = generateMaze()
    print(endPos)
    bfs(maze, startPos, endPos)

def partTwo():
    maze, _, endPos = generateMaze()
    startPositions = []
    for yi in range(0, len(maze)):
        for xi in range(0, len(maze[0])):
            if maze[yi][xi] == 0:
                startPositions.append((yi, xi))
    allValues = map(lambda x: bfs(maze, x, endPos), startPositions)
    print(min(allValues))

def generateMaze():
    maze = []
    row = 0
    rowStart = 0
    colStart = 0
    rowEnd = 0
    colEnd = 0
    with open("input.txt") as f:
        for line in f:
            col = line.find("S")
            if col != -1:
                colStart = col
                rowStart = row

            col = line.find("E")
            if col != -1:
                colEnd = col
                rowEnd = row
            maze.append([ord(i) - 97 if ord(i) > 96 else 0 if i == "S" else 25 for i in line.strip()])
            row += 1
    return maze, (rowStart, colStart), (rowEnd, colEnd)

def generateAdj(pos, dimX, dimY):
    y, x = pos
    allPos = [(y , x - 1), (y , x + 1), (y - 1, x), (y + 1, x)]
    allValidPos = filter(lambda node: node[0] >= 0 and node[1] >=0 and node[0] < dimY and node[1] < dimX, allPos)
    return list(allValidPos)

def bfs(maze, startPos, endPos):
    dimY = len(maze)
    dimX = len(maze[0])
    visited = [[False for _ in range(0, dimX)] for _ in range(0, dimY)]
    level = 1
    visited[0][0] = True
    frontier = deque([startPos])
    currentLevelNodes = 1
    nextLevelNodes = 0
    while True:
        if currentLevelNodes <= 0:
            currentLevelNodes = nextLevelNodes
            nextLevelNodes = 0
            level += 1
        if not frontier:
            return 9999999999
        nextNode = frontier.popleft()
        currentLevelNodes -= 1
        nextNodes = generateAdj(nextNode, dimX=dimX, dimY=dimY)
        allValidNodes = list(filter(lambda node: \
            not visited[node[0]][node[1]] and maze[node[0]][node[1]] <= maze[nextNode[0]][nextNode[1]] + 1,
            nextNodes))
        for node in allValidNodes:
            nextLevelNodes += 1
            visited[node[0]][node[1]] = True
            if node == endPos:
                print(level)
                break
        if visited[endPos[0]][endPos[1]]:
            break
        frontier.extend(allValidNodes)
    
    return level 

if __name__ == "__main__":
    main()