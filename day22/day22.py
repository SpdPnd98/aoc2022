def main():
    partTwo()

playerDir = 0

def partOne():
    maze, actions = parseMaze()
    nextLoc = (maze[0][1], 0)
    print(nextLoc)
    for item in actions:
        if isinstance(item, int):
            nextLoc = moveBy(maze, nextLoc, item)
        else:
            rotatePlayer(item)
    print(nextLoc)
    print(playerDir)
    print(1000 * (nextLoc[1] + 1) + 4 * (nextLoc[0] + 1) + playerDir)

def accessMaze(maze, x, y):
    if y < 0 or x < 0 or y >= len(maze) or x >= len(maze[y][0]):
        return False
    return maze[y][0][x]

def moveBy(maze, startPos, numberOfSteps):
    startX, startY = startPos
    if playerDir == 0:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevX = startX
            startX += 1
            if accessMaze(maze, startX, startY):
                continue
            if startX == len(maze[startY][0]):
                startX = maze[startY][1]
            if accessMaze(maze, startX, startY):
                continue
            else:
                startX = prevX # revert step, cannot move anymore
                break
        return (startX, startY)
    elif playerDir == 1:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevY = startY
            startY += 1
            if accessMaze(maze, startX, startY):
                continue
            if startY == len(maze) or startX < maze[startY][1] or startX >= len(maze[startY][0]):
                startY = prevY
                while startY >= 0 and maze[startY][1] <= startX and startX < len(maze[startY][0]):
                    startY -= 1
                startY += 1 # offset back
            if accessMaze(maze, startX, startY):
                continue
            else:
                startY = prevY # revert step, cannot move anymore
                break
        return (startX, startY)
    elif playerDir == 2:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevX = startX
            startX -= 1
            if accessMaze(maze, startX, startY):
                continue
            if startX < maze[startY][1]:
                startX = len(maze[startY][0]) - 1
            if accessMaze(maze, startX, startY):
                continue
            else:
                startX = prevX # revert step, cannot move anymore
                break
        return (startX, startY)
    elif playerDir == 3:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevY = startY
            startY -= 1
            if accessMaze(maze, startX, startY):
                continue
            if startY < 0 or startX < maze[startY][1] or startX >= len(maze[startY][0]):
                startY = prevY
                while startY < len(maze) and maze[startY][1] <= startX and startX < len(maze[startY][0]):
                    startY += 1
                startY -= 1 # offset back
            if accessMaze(maze, startX, startY):
                continue
            else:
                startY = prevY # revert step, cannot move anymore
                break
        return (startX, startY)

def moveInCube(maze, startPos, numberOfSteps):
    global playerDir
    startX, startY = startPos
    originalHeading = playerDir
    if playerDir == 0:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevX = startX
            startX += 1
            newX = startX
            newY = startY
            if startX == len(maze[startY][0]):
                newX, newY = wrapToNext((prevX, startY))
                # print(newX, newY)
            if accessMaze(maze, newX, newY):
                if (originalHeading != playerDir):
                    return moveInCube(maze, (newX, newY), numberOfSteps)
                startX = newX
                startY = newY
                continue
            else:
                startX = prevX # revert step, cannot move anymore
                playerDir = originalHeading
                break
        return (startX, startY)
    elif playerDir == 1:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevY = startY
            startY += 1
            newX = startX
            newY = startY
            if startY == len(maze) or startX < maze[startY][1] or startX >= len(maze[startY][0]):
                newX, newY = wrapToNext((startX, prevY))
                # print("Warp to next:", (newX, newY))
            if accessMaze(maze, newX, newY):
                if (originalHeading != playerDir):
                    return moveInCube(maze, (newX, newY), numberOfSteps)
                startX = newX
                startY = newY
                continue
            else:
                startY = prevY # revert step, cannot move anymore
                playerDir = originalHeading
                break
        return (startX, startY)
    elif playerDir == 2:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevX = startX
            startX -= 1
            newX = startX
            newY = startY
            if startX < maze[startY][1]:
                newX, newY = wrapToNext((prevX, startY))
                # print(newX, newY)
            if accessMaze(maze, newX, newY):
                if (originalHeading != playerDir):
                    return moveInCube(maze, (newX, newY), numberOfSteps)
                startX = newX
                startY = newY
                continue
            else:
                startX = prevX # revert step, cannot move anymore
                playerDir = originalHeading
                break
        return (startX, startY)
    elif playerDir == 3:
        while numberOfSteps > 0:
            numberOfSteps -= 1
            prevY = startY
            startY -= 1
            newX = startX
            newY = startY
            if startY < 0 or startX < maze[startY][1] or startX >= len(maze[startY][0]):
               newX, newY = wrapToNext((startX, prevY))
            if accessMaze(maze, newX, newY):
                if (originalHeading != playerDir):
                    return moveInCube(maze, (newX, newY), numberOfSteps)
                startX = newX
                startY = newY
                continue
            else:
                startY = prevY # revert step, cannot move anymore
                playerDir = originalHeading
                break
        return (startX, startY)

def partTwo():
    global playerDir
    maze, actions = parseMaze()
    nextLoc = (maze[0][1], 0)
    playerDir = 0
    print(nextLoc)
    for item in actions:
        if isinstance(item, int):
            nextLoc = moveInCube(maze, nextLoc, item)
            print(item, nextLoc, playerDir)
        else:
            rotatePlayer(item)
            print(item, nextLoc, playerDir)
    print(nextLoc)
    print(playerDir)
    print(1000 * (nextLoc[1] + 1) + 4 * (nextLoc[0] + 1) + playerDir)
    # playerDir = 2
    # nextLoc = (64, 26)
    # print(accessMaze(maze, nextLoc[0], nextLoc[1]))
    # newLoc = moveInCube(maze, nextLoc, 20)
    # print(newLoc)
    # print(playerDir)

def parseMaze():
    with open("input.txt") as f:
        maze = []
        while True:
            line = f.readline()[:-1]
            if not line:
                break
            col = []
            offset = 0
            for char in line:
                if char == " ":
                    offset += 1
                col.append(char == ".")
            maze.append((col, offset))
        rawActions = f.readline()[:-1]
        getForward = True
        actions = []
        start = 0
        end = 0
        for i, char in enumerate(rawActions):
            if getForward:
                end += 1
                if end == len(rawActions) or ord(rawActions[end]) > 57:
                    getForward = False
                    actions.append(int(rawActions[start:end]))
            else:
                start = i + 1
                end = i + 1
                actions.append(char)
                getForward = True
        return maze, actions

def transition(origin, nextFace): # turn coordinates, note that y is inverted, so cc -> c and vice versa
    if (origin == 1 and nextFace == 2) or (origin == 2 and nextFace == 1):
        return lambda x, y: (x, y) # original direction
    elif (origin == 1 and nextFace == 4) or (origin == 4 and nextFace == 1):
        rotatePlayer('R')
        rotatePlayer('R')
        return lambda x, y: (-x, -y) # turn 180 degrees
    elif (origin == 1 and nextFace == 3) or (origin == 3 and nextFace == 1):
        return lambda x, y: (x, y) # original direction
    elif (origin == 1 and nextFace == 6):
        rotatePlayer('R')
        return lambda x, y: (-y, x) # turn 90 deg clockwise
    elif (origin == 2 and nextFace == 6) or (origin == 6 and nextFace == 2):
        return lambda x, y: (x, y) # original direction
    elif (origin == 2 and nextFace == 3):
        rotatePlayer('R')
        return lambda x, y: (-y, x) # turn 90 deg clockwise
    elif (origin == 2 and nextFace == 5) or (origin == 5 and nextFace == 2):
        rotatePlayer('R')
        rotatePlayer('R')
        return lambda x, y: (-x, -y) # turn 180 degree
    elif (origin == 3 and nextFace == 2) or (origin == 3 and nextFace == 4):
        rotatePlayer('L')
        return lambda x, y: (y, -x) # turn 90 degree counterclockwise
    elif (origin == 3 and nextFace == 5) or (origin == 5 and nextFace == 3):
        return lambda x, y: (x, y) # original direction
    elif (origin == 4 and nextFace == 5) or (origin == 5 and nextFace == 4):
        return lambda x, y: (x, y) # original direction
    elif (origin == 4 and nextFace == 6) or (origin == 6 and nextFace == 4):
        return lambda x, y: (x, y) # original direction
    elif (origin == 4 and nextFace == 3):
        rotatePlayer('R')
        return lambda x, y: (-y, x) # turn 90 deg clockwise
    elif (origin == 5 and nextFace == 6):
        rotatePlayer('R')
        return lambda x, y: (-y, x) # turn 90 deg clockwise
    elif (origin == 6 and nextFace == 5) or (origin == 6 and nextFace == 1):
        rotatePlayer('L')
        return lambda x, y: (y, -x) # turn 90 deg counterclockwise
    else:
        print("should not reach here", origin, nextFace)

def wrapToNext(currentPos):
    x, y = currentPos
    currentCenter = faceCenter[faceIndex(x, y)]
    if faceIndex(x, y) == 1:
        relativePos = (x - currentCenter[0], y - currentCenter[1])
        if playerDir == 0: # wrap right to left
            newRelative = transition(1, 2)(relativePos[0] - 49 , relativePos[1] )
            return (int(faceCenter[2][0] + newRelative[0]) , int(faceCenter[2][1] + newRelative[1]))
        if playerDir == 1: # wrap down to up
            newRelative = transition(1, 3)(relativePos[0] , relativePos[1] - 49 )
            return (int(faceCenter[3][0] + newRelative[0]), int(faceCenter[3][1] + newRelative[1]))
        if playerDir == 2: # wrap left to right
            # print(relativePos)
            newRelative = transition(1, 4)(relativePos[0] + 49 , relativePos[1])
            # print(newRelative)
            return (int(faceCenter[4][0] + newRelative[0]), int(faceCenter[4][1] + newRelative[1]))
        if playerDir == 3: # wrap up to down
            newRelative = transition(1, 6)(relativePos[0] , relativePos[1] + 49 )
            # print((int(faceCenter[6][0] + newRelative[0]), int(faceCenter[6][1] + newRelative[1])))
            return (int(faceCenter[6][0] + newRelative[0]), int(faceCenter[6][1] + newRelative[1]))
        return -1
    elif faceIndex(x, y) == 2:
        relativePos = (x - currentCenter[0], y - currentCenter[1])
        if playerDir == 0:
            newRelative = transition(2, 5)(relativePos[0] - 49, relativePos[1] )
            return (int(newRelative[0] + faceCenter[5][0]), int(newRelative[1] + faceCenter[5][1]))
        if playerDir == 1:
            # print(relativePos, currentPos)
            newRelative = transition(2, 3)(relativePos[0] , relativePos[1] - 49)
            # print(newRelative)
            return (int(faceCenter[3][0] + newRelative[0]), int(faceCenter[3][1] + newRelative[1]))
        if playerDir == 2:
            newRelative = transition(2, 1)(relativePos[0] + 49 , relativePos[1] )
            return (int(newRelative[0] + faceCenter[1][0]), int(newRelative[1] + faceCenter[1][1]))
        if playerDir == 3:
            newRelative = transition(2, 6)(relativePos[0] , relativePos[1] + 49)
            return (int(newRelative[0] + faceCenter[6][0]), int(newRelative[1] + faceCenter[6][1] ))
        return -1
    elif faceIndex(x, y) == 3:
        relativePos = (x - currentCenter[0], y - currentCenter[1])
        if playerDir == 0:
            newRelative = transition(3, 2)(relativePos[0] - 49 , relativePos[1])
            # print(newRelative)
            return (int( faceCenter[2][0] + newRelative[0]), int(faceCenter[2][1] + newRelative[1]))
        if playerDir == 1:
            newRelative = transition(3, 5)(relativePos[0] , relativePos[1] - 49 )
            return (int(faceCenter[5][0] + newRelative[0]), int(faceCenter[5][1] + newRelative[1]))
        if playerDir == 2:
            # print(relativePos)
            newRelative = transition(3, 4)(relativePos[0] + 49 , relativePos[1])
            # print(newRelative)
            return (int(faceCenter[4][0] + newRelative[0]), int(faceCenter[4][1] + newRelative[1]))
        if playerDir == 3:
            newRelative = transition(3, 1)(relativePos[0] , relativePos[1] + 49)
            return (int(faceCenter[1][0] + newRelative[0]), int(faceCenter[1][1] + newRelative[1]))
        return -1
    elif faceIndex(x, y) == 4:
        relativePos = (x - currentCenter[0], y - currentCenter[1])
        if playerDir == 0:
            newRelative = transition(4, 5)(relativePos[0] - 49 , relativePos[1] )
            return (int(newRelative[0] + faceCenter[5][0]), int(newRelative[1] + faceCenter[5][1]))
        if playerDir == 1:
            newRelative = transition(4, 6)(relativePos[0] , relativePos[1] - 49)
            return (int(newRelative[0] + faceCenter[6][0]), int(newRelative[1] + faceCenter[6][1]))
        if playerDir == 2:
            newRelative = transition(4, 1)(relativePos[0] + 49 , relativePos[1] )
            return (int(newRelative[0] + faceCenter[1][0]), int(newRelative[1] + faceCenter[1][1]))
        if playerDir == 3:
            newRelative = transition(4, 3)(relativePos[0] , relativePos[1] + 49 )
            return (int(newRelative[0] + faceCenter[3][0]), int(newRelative[1] + faceCenter[3][1]))
        return -1
    elif faceIndex(x, y) == 5:
        relativePos = (x - currentCenter[0], y - currentCenter[1])
        if playerDir == 0:
            newRelative = transition(5, 2)(relativePos[0] -49 , relativePos[1] )
            return (int(newRelative[0] + faceCenter[2][0]), int(newRelative[1] + faceCenter[2][1]))
        if playerDir == 1:
            newRelative = transition(5, 6)(relativePos[0] , relativePos[1] - 49 )
            return (int(newRelative[0] + faceCenter[6][0]), int(newRelative[1] + faceCenter[6][1]))
        if playerDir == 2:
            newRelative = transition(5, 4)(relativePos[0] + 49 , relativePos[1] )
            return (int(newRelative[0] + faceCenter[4][0]), int(newRelative[1] + faceCenter[4][1]))
        if playerDir == 3:
            newRelative = transition(5, 3)(relativePos[0] , relativePos[1] + 49 )
            return (int(newRelative[0] + faceCenter[3][0]), int(newRelative[1] + faceCenter[3][1]))
        return -1
    elif faceIndex(x, y) == 6:
        relativePos = (x - currentCenter[0], y - currentCenter[1])
        if playerDir == 0:
            newRelative = transition(6, 5)(relativePos[0] - 49 , relativePos[1] )
            return (int(newRelative[0] + faceCenter[5][0]), int(newRelative[1] + faceCenter[5][1]))
        if playerDir == 1:
            newRelative = transition(6, 2)(relativePos[0] , relativePos[1] - 49 )
            return (int(newRelative[0] + faceCenter[2][0]), int(newRelative[1] + faceCenter[2][1]))
        if playerDir == 2:
            newRelative = transition(6, 1)(relativePos[0] + 49 , relativePos[1])
            return (int(newRelative[0] + faceCenter[1][0]), int(newRelative[1] + faceCenter[1][1]))
        if playerDir == 3:
            newRelative = transition(6, 4)(relativePos[0] , relativePos[1] + 49 )
            return (int(newRelative[0]+ faceCenter[4][0]), int(newRelative[1] + faceCenter[4][1]))
        return -1
    else:
        print("This should not happen")

def faceIndex(x, y):
    if 0 <= y < 50 and 50 <= x < 100:
        return 1
    elif 0 <= y < 50 and 100 <= x < 150:
        return 2
    elif 50 <= y < 100 and 50 <= x < 100:
        return 3
    elif 100 <= y < 150 and 0 <= x < 50:
        return 4
    elif 100 <= y < 150 and 50 <= x < 100:
        return 5
    elif 150 <= y < 200 and 0 <= x < 50:
        return 6
    else:
        return -1

faceCenter = {
    1: (74.5,  24.5),
    2: (124.5, 24.5),
    3: (74.5,  74.5),
    4: (24.5,  124.5),
    5: (74.5,  124.5),
    6: (24.5,  174.5),
}     


def rotatePlayer(direction):
    global playerDir
    if direction == "R":
        playerDir = (playerDir + 1) % 4
    else:
        playerDir = (playerDir - 1) % 4

if __name__ == "__main__":
    main()