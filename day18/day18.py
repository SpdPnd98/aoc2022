def main():
    # partOne()
    partTwo()

def partOne():
    with open("input.txt") as f:
        faces = set()
        coveredFaces = 0
        for line in f:
            x, y, z = [int(item) for item in line.strip("\n").split(",")]
            cubeFaces = generateFaces(x, y, z)
            for face in cubeFaces:
                isSimilar = False
                for storedFace in faces:
                    if checkSimilarFaces(face, storedFace):
                        isSimilar = True
                        faces.remove(face)
                        coveredFaces += 1
                        break
                if not isSimilar:
                    faces.add(face)
        print(len(faces))
            

def generateFaces(x, y,z):
    faces = []
    faces.append(((x, y, z), (x-1, y, z), (x-1, y-1, z), (x, y-1, z)))
    faces.append(((x, y, z), (x-1, y, z), (x-1, y, z-1), (x, y, z-1)))
    faces.append(((x, y, z), (x, y-1, z), (x, y-1, z-1), (x, y, z-1)))
    faces.append(((x-1, y, z), (x-1, y-1, z), (x-1, y-1, z-1), (x-1, y, z-1)))
    faces.append(((x, y, z-1), (x-1, y, z-1), (x-1, y-1, z-1), (x, y-1, z-1)))
    faces.append(((x, y-1, z), (x-1, y-1, z), (x-1, y-1, z-1), (x, y-1, z-1)))
    return faces

def checkSimilarFaces(face1, face2):
    return set(face1) == set(face2)

def partTwo():
    with open("input.txt") as f:
        cubes = []
        for line in f:
            x, y, z = [int(item) for item in line.strip("\n").split(",")]
            cubes.append((x,y,z))
        faces = floodFill(cubes)
        print(faces)

cubeDeltas = {}

def floodFill(cubes):
    maxX = 0
    maxY = 0
    maxZ = 0

    minX = 999999
    minY = 999999
    minZ = 999999


    for cube in cubes:
        maxX = max(cube[0], maxX)
        maxY = max(cube[1], maxY)
        maxZ = max(cube[2], maxZ)

        minX = min(cube[0], minX)
        minY = min(cube[1], minY)
        minZ = min(cube[2], minZ)

    def within(x, y, z):
        return minX - 1 <= x and x <= maxX + 1 and minY - 1 <= y and y <= maxY + 1 and minZ - 1 <= z and z <= maxZ + 1
    generatedFill = generateFill(cubes, (minX-1, minY-1, minZ-1), within)

    numFaces = 0
    for cube in cubes:
        for neighbour in generateSixNeighbours(cube):
            numFaces += 1 if neighbour in generatedFill else 0 # this is equivalent to generating 6 faces
    
    return numFaces

def generateSixNeighbours(coordinates):
    x, y, z = coordinates
    return [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x,y,z+1)]

def generateFill(cubes, startCoordinate, withinFunction):
    cubesSet = set(cubes) # use hash table is faster
    seenPerimeter = set()
    fillInCubes = [startCoordinate]

    while fillInCubes:
        potX, potY, potZ = fillInCubes.pop()
        # print("Added to seen Perimeter:", (potX, potY, potZ))
        seenPerimeter.add((potX, potY, potZ))
        potNeighbours = generateSixNeighbours((potX, potY, potZ))
        # print("Pot neighbours:", potNeighbours)
        for neighbour in potNeighbours:
            nX, nY, nZ = neighbour
            if withinFunction(nX, nY, nZ):
                if neighbour not in seenPerimeter and neighbour not in cubesSet:
                    fillInCubes.append(neighbour)
    
    return seenPerimeter

if __name__ == "__main__":
    main()