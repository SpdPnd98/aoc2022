def main():
    partTwo()

def generatePerimeter(xCenter=500, yCenter=0):
    area = {}
    with open("input.txt") as f:
        maxX = 0
        minX = 0
        maxY = 0
        minY = 0
        for line in f:
            allCoordinates = [(int(point.split(",")[0]) - xCenter, int(point.split(",")[1]) - yCenter) for point in line[:-1].split(" -> ")]
            for i in range(0, len(allCoordinates) - 1):
                subMaxX = max(allCoordinates[i][0], allCoordinates[i+1][0])
                subMinX = min(allCoordinates[i][0], allCoordinates[i+1][0])
                subMaxY = max(allCoordinates[i][1], allCoordinates[i+1][1])
                subMinY = min(allCoordinates[i][1], allCoordinates[i+1][1])
                maxX = max(maxX, subMaxX)
                minX = min(minX, subMinX)
                maxY = max(maxY, subMaxY)
                minY = min(minY, subMinY)

                # either draw a straight up line or straight horizontal line
                for x in range(subMinX, subMaxX + 1):
                    newCoordinate = (x, allCoordinates[i][1])
                    area[newCoordinate] = True
                for y in range(subMinY, subMaxY + 1):
                    newCoordinate = (allCoordinates[i][0], y)
                    area[newCoordinate] = True
            
            # draw other boxes, additionally add a perimeter
            for x in range(minX - 1, maxX + 2):
                for y in range(minY, maxY + 2): # usually, Y would not go beyond 0, semantically not valid
                    if (x,y) not in area:
                        area[(x, y)] = False
    return area, maxX, maxY, minX, minY

def tick(area, source, maxX, maxY, minX, minY):
    x, y = source
    nextLoc = (x, y+1)
    while nextLoc[1] < maxY + 1:
        if nextLoc not in area:
            return nextLoc # happens if exceed min/max x, of which it will then drop to abyss
        if area[nextLoc]:
            newNextLoc = (nextLoc[0] + (-1 if not area[(nextLoc[0] - 1, nextLoc[1])]\
                 else 1 if not area[(nextLoc[0] + 1, nextLoc[1])] else 0), nextLoc[1])
            if newNextLoc == nextLoc:
                return (nextLoc[0], nextLoc[1] - 1)
            elif newNextLoc[0] > maxX or newNextLoc[0] < minX or newNextLoc[1] > maxY:
                return nextLoc
            else:
                nextLoc = newNextLoc
        else:
            nextLoc = (nextLoc[0], nextLoc[1] + 1)
    
    return nextLoc # only happens if it exceeds the perimeter

def printArea(area, maxX, maxY, minX, minY):
    for y in range(minY, maxY + 1):
        toShow = ""
        for x in range(minX, maxX + 1):
            toShow += "#" if area[(x, y)] else "."
        print(toShow)
    print()

def partOne(): # get second last iteration value
    sandbox, maxX, maxY, minX, minY = generatePerimeter()
    printArea(sandbox, maxX, maxY, minX, minY)
    previousTick = (0, 0)
    numTicks = 0
    while True:
        nextTick = tick(sandbox, (0,0), maxX, maxY, minX, minY)
        if nextTick == previousTick:
            break
        sandbox[nextTick] = True
        numTicks += 1
        previousTick = nextTick
        print(numTicks)
        printArea(sandbox, maxX, maxY, minX, minY)

    # print(numTicks)
    # nexLoc = tick(sandbox, (0,0), maxY)
    # print(nexLoc)
    # printArea(sandbox, maxX, maxY, minX, minY)

def generatePerimeterGround(xCenter=500, yCenter=0):
    area = {}
    with open("input.txt") as f:
        maxX = 0
        minX = 0
        maxY = 0
        minY = 0
        for line in f:
            allCoordinates = [(int(point.split(",")[0]) - xCenter, int(point.split(",")[1]) - yCenter) for point in line[:-1].split(" -> ")]
            for i in range(0, len(allCoordinates) - 1):
                subMaxX = max(allCoordinates[i][0], allCoordinates[i+1][0])
                subMinX = min(allCoordinates[i][0], allCoordinates[i+1][0])
                subMaxY = max(allCoordinates[i][1], allCoordinates[i+1][1])
                subMinY = min(allCoordinates[i][1], allCoordinates[i+1][1])
                maxX = max(maxX, subMaxX)
                minX = min(minX, subMinX)
                maxY = max(maxY, subMaxY)
                minY = min(minY, subMinY)

                # either draw a straight up line or straight horizontal line
                for x in range(subMinX, subMaxX + 1):
                    newCoordinate = (x, allCoordinates[i][1])
                    area[newCoordinate] = True
                for y in range(subMinY, subMaxY + 1):
                    newCoordinate = (allCoordinates[i][0], y)
                    area[newCoordinate] = True
            
            # draw other boxes, additionally add a perimeter
            for x in range(minX - 1, maxX + 2):
                for y in range(minY, maxY + 2): # usually, Y would not go beyond 0, semantically not valid
                    if (x,y) not in area:
                        area[(x, y)] = False

    for x in range(minX - 1, maxX + 2):
        area[(x, maxY+2)] = True
    return area, maxX, maxY+2, minX, minY

def expandArea(area, x, maxX, minX, maxY):
    if x <= minX or x >= maxX :
        print("expanding")
        for yi in range(0, maxY): # the last item is the border, keep as true
            area[(maxX+1), yi] = False
            area[(maxX+2), yi] = False
            area[(minX-1), yi] = False
            area[(minX-2), yi] = False
        area[(maxX+1, maxY)] = True
        area[(maxX+2, maxY)] = True
        area[(minX-1, maxY)] = True
        area[(minX-2, maxY)] = True
        minX = minX - 2
        maxX = maxX + 2
    return maxX, minX


def expandingTick(area, source, maxX, maxY, minX, minY):
    x, y = source
    nextLoc = (x, y+1)
    while nextLoc[1] < maxY + 1:
        if nextLoc not in area:
            return nextLoc, maxX, maxY, minX, minY # happens if exceed min/max x, of which it will then drop to abyss
        if area[nextLoc]:
            maxX, minX = expandArea(area, nextLoc[0] - 1, maxX, minX, maxY)
            maxX, minX = expandArea(area, nextLoc[0] + 1, maxX, minX, maxY)
            newNextLoc = (nextLoc[0] + (-1 if not area[(nextLoc[0] - 1, nextLoc[1])]\
                 else 1 if not area[(nextLoc[0] + 1, nextLoc[1])] else 0), nextLoc[1])
            if newNextLoc == nextLoc:
                return (nextLoc[0], nextLoc[1] - 1), maxX, maxY, minX, minY
            elif newNextLoc[0] > maxX or newNextLoc[0] < minX or newNextLoc[1] > maxY:
                return nextLoc, maxX, maxY, minX, minY
            else:
                nextLoc = newNextLoc
        else:
            nextLoc = (nextLoc[0], nextLoc[1] + 1)
    
    return nextLoc, maxX, maxY, minX, minY # only happens if it exceeds the perimeter

def partTwo(): # get last iteration value
    sandbox, maxX, maxY, minX, minY = generatePerimeterGround()
    printArea(sandbox, maxX, maxY, minX, minY)
    previousTick = (0, 0)
    numTicks = 0
    while True:
        nextTick, maxX, maxY, minX, minY = expandingTick(sandbox, (0,0), maxX, maxY, minX, minY)
        if nextTick == previousTick:
            printArea(sandbox, maxX, maxY, minX, minY)
            print(numTicks)
            break
        sandbox[nextTick] = True
        numTicks += 1
        previousTick = nextTick
        

if __name__ == "__main__":
    main()