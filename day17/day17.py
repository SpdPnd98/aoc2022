from math import floor

def main():
    # partOne()
    partTwo()

def partOne():
    with open("input.txt") as f:
        airSequence = AirSequence(f.readline().strip())
        numOfRocks = 20
        originalRocks = numOfRocks
        drop = False
        board = Board()
        # print(board.highest)
        # print(board)
        nextStartingHeight = board.highest + 3
        pieceHeight, nextPieceCoordinates, _ = GeneratePieceCoordinates.getNextPiece(nextStartingHeight)
        _ = board.increaseBoardHeight(nextStartingHeight + pieceHeight)
        while numOfRocks > 0:
            if drop:
                # print(nextStartingHeight)
                # print(nextPieceCoordinates)
                status, nextPieceCoordinates = board.stepFall(nextPieceCoordinates)
                # print(board)
            else:
                # print(nextStartingHeight)
                # print(nextPieceCoordinates)
                status, nextPieceCoordinates = board.stepGush(nextPieceCoordinates, airSequence)
                # print(board)
            if status:
                numOfRocks -= 1
                print("Rock: " , (originalRocks - numOfRocks))
                pieceHeight, nextPieceCoordinates, _ = GeneratePieceCoordinates.getNextPiece(board.highest + 4)
                _ = board.increaseBoardHeight(board.highest + 3 + pieceHeight)
            drop = not drop
        print(board.highest)

def partTwo():
    with open("input.txt") as f:
        airSequence = AirSequence(f.readline().strip())
        numOfRocks = 1000000000000
        originalRocks = numOfRocks
        drop = False
        board = Board()
        # print(board.highest)
        # print(board)
        nextStartingHeight = board.highest + 3
        pieceHeight, originalPieceCoordinates, pieceIndex = GeneratePieceCoordinates.getNextPiece(nextStartingHeight)
        _ = board.increaseBoardHeight(nextStartingHeight + pieceHeight)
        storedHeight = None
        frontiers = {}
        nextPieceCoordinates = originalPieceCoordinates
        while numOfRocks > 0:
            if drop:
                status, nextPieceCoordinates = board.stepFall(nextPieceCoordinates)
            else:
                status, nextPieceCoordinates = board.stepGush(nextPieceCoordinates, airSequence)

            # if storedHeight is None and board.findRepeat(airSequence):
            #     print("Repeat Found....")
            #     print(board)
            #     numberOfRocksRepeating = (originalRocks - numOfRocks) // 2
            #     numRepeats = numOfRocks // numberOfRocksRepeating
            #     numOfRocks = originalRocks % numberOfRocksRepeating
            #     storedHeight = numRepeats * (board.highest // 2)

            if status:
                numOfRocks -= 1
                print("Rock: " , (originalRocks - numOfRocks))
                if storedHeight is None:
                    currentRockNum = originalRocks - numOfRocks
                    frontier = board.generateFrontierData()
                    currentSequenceIndex = airSequence.getCurrentCount()
                    currrentFrontierData = (currentSequenceIndex, frontier, pieceIndex, board.highest)
                    similarFrontiers = getAllSimilar(currrentFrontierData, frontiers)
                    frontiers[currentRockNum] = currrentFrontierData


                    # for ind in similarFrontiers:
                    #     bottomRockInd = ind - 1
                    #     bottomRockStart = bottomRockInd
                    #     topRockInd = currentRockNum - 1
                    #     topRockStart = topRockInd
                    #     checked = False
                    #     while bottomRockStart >= 0 and topRockStart != bottomRockInd:
                    #         if not checked:
                    #             checked = True
                    #         if frontiers[topRockStart] != frontiers[bottomRockStart]: # note changed of frontiers include highest at board
                    #             break
                    #         topRockStart -= 1
                    #         bottomRockStart -= 1
                            
                    #     if checked and topRockStart == bottomRockInd:
                    #         print("Repeat has been detected")
                    #         return

                    deltas = []
                    for i in range(0, len(similarFrontiers) - 1):
                        deltas.append(similarFrontiers[i + 1] - similarFrontiers[i])
                    
                    for i in range(len(deltas) - 1, -1, -1):
                        foundJ = False
                        for j in range(i - 1, -1, -1):
                            if deltas[i] == deltas[j]:
                                currentI = i - 1
                                currentJ = j - 1
                                while currentI >= 0 and currentJ >= 0 and currentI != j:
                                    if similarFrontiers[currentI] != similarFrontiers[currentJ]:
                                        break
                                if currentI == j:
                                    # print(deltas)
                                    # print(similarFrontiers)
                                    foundJ = True
                                    deltaSum = sum(deltas[j:i])
                                    heightDifference = abs(frontiers[similarFrontiers[j+1]][3] - frontiers[similarFrontiers[j]][3])
                                    leftIterations = numOfRocks % deltaSum
                                    replicaIndices = floor((numOfRocks - leftIterations)/deltaSum) # number of replications
                                    print("Rocks left:", numOfRocks)
                                    storedHeight = replicaIndices * heightDifference
                                    print("Repeat has been found at recurring deltas %s, deltaSum=%d, recurring count between %d - %d, heights generated %d" %(deltas[j:i], deltaSum, numOfRocks, leftIterations, heightDifference * replicaIndices))
                                    numOfRocks = leftIterations
                                break
                        if foundJ: break
                        print("Cannot find similar yet: %s, %s" %(similarFrontiers, deltas))
                
                pieceHeight, originalPieceCoordinates, pieceIndex = GeneratePieceCoordinates.getNextPiece(board.highest + 4)
                nextPieceCoordinates = originalPieceCoordinates
                _ = board.increaseBoardHeight(board.highest + 3 + pieceHeight)

            drop = not drop
        # print("Board highest: %d" %(board.highest))
        print(board.highest if storedHeight is None else board.highest + storedHeight)

def getAllSimilar(frontierData, prevFrontiers):
    indices = []
    for ind in prevFrontiers:
        print("%s vs %s" %(frontierData, prevFrontiers[ind]))
        if frontierData[0] == prevFrontiers[ind][0] and frontierData[1] == prevFrontiers[ind][1] and frontierData[2] == prevFrontiers[ind][2]:
            indices.append(ind)
    return indices

class Board:
    def __init__(self):
        self.width = 7
        self.boardState = [[True for _ in range(0, self.width)], [False for _ in range(0, self.width)]]
        self.highest = 1
    
    def increaseBoardHeight(self, increment=0):
        # print(len(self.boardState))
        # print(self.highest + increment)
        for _ in range(0, (self.highest + increment) - len(self.boardState) + 1):
            self.boardState += [[False for _ in range(0, self.width)]]
        return self.highest + increment

    def stepGush(self, oldPieceCoordinates, airSequence):
        nextAir = airSequence.getNext()
        newCoordinates = []
        for piece in oldPieceCoordinates:
            self.boardState[piece[1]][piece[0]] = False # remove piece
            newCoordinates.append((piece[0] + nextAir, piece[1])) # implementt rules for air gushes
        
        moveState = self.gushable(newCoordinates)
        # print("Gush %s %s" %(newCoordinates, moveState))

        if moveState == 1:
            for piece in newCoordinates:
                self.boardState[piece[1]][piece[0]] = True
            return False, newCoordinates
        else:
            for piece in oldPieceCoordinates:
                self.boardState[piece[1]][piece[0]] = True # readd the piece back
            return False, oldPieceCoordinates # generate next piece if landed
    
    def stepFall(self, oldPieceCoordinates):
        newCoordinates = []
        for piece in oldPieceCoordinates:
            self.boardState[piece[1]][piece[0]] = False # remove piece
            newCoordinates.append((piece[0], piece[1] - 1))

        moveState = self.gushable(newCoordinates)
        # print("Fall %s %s" %(newCoordinates, moveState))

        if moveState == 1:
            for piece in newCoordinates:
                self.boardState[piece[1]][piece[0]] = True
            return False, newCoordinates
        elif moveState == -1:
            maxY = 0
            for piece in oldPieceCoordinates:
                self.boardState[piece[1]][piece[0]] = True # readd the piece back
                maxY = max(maxY, piece[1])
            self.highest = max(self.highest, maxY)
            return moveState == -1, oldPieceCoordinates # generate next piece

    def gushable(self, newPieceCoordinates):
        for piece in newPieceCoordinates:
            if piece[0] < self.width and piece[0] >= 0 and self.boardState[piece[1]][piece[0]]:
                return -1 # land on piece
            elif piece[0] >= self.width or piece[0] < 0:
                return 0 # blocked state
        return 1 # can move

    def generateFrontierData(self):
        frontier = []
        maxY = 0
        for x in range(0, self.width):
            for y in range(len(self.boardState) - 1, -1, -1):
                if self.boardState[y][x]:
                    maxY = max(maxY, y)
                    frontier.append(y)
                    break
        
        return tuple([height - maxY for height in frontier])

    def __str__(self):
        representation = ""
        for y in range(0, len(self.boardState)):
            temp = "|"
            for x in range(0, len(self.boardState[y])):
                temp += "#" if self.boardState[y][x] else "."
            representation = temp + "|\n" + representation
        return representation

class AirSequence:
    @staticmethod
    def parseAir(sequence):
        numericSequence = [-1 if seq == "<" else 1 for seq in sequence]
        return numericSequence
    def __init__(self, sequence):
        self.sequence = AirSequence.parseAir(sequence)
        self.count = 0
    
    def getNext(self):
        nextItem = self.sequence[self.count]
        self.count = (self.count + 1) % len(self.sequence)
        return nextItem
    
    def getCurrentCount(self):
        return self.count

class GeneratePieceCoordinates:
    pieces = [[0, [(2,0), (3,0), (4,0), (5,0)], 1],
              [2, [(3,0), (2,1), (3,1), (4,1), (3,2)], 2],
              [2, [(2,0), (3,0), (4,0), (4,1), (4,2)], 3],
              [3, [(2,0), (2,1), (2,2), (2,3)], 4],
              [1, [(2,0), (2,1), (3,0), (3,1)], 5]]
    count = 0
    @staticmethod
    def getNextPiece(height):
        nextPiece = GeneratePieceCoordinates.pieces[GeneratePieceCoordinates.count]
        nextPieceOffset = []
        for coordinate in nextPiece[1]:
            nextPieceOffset.append((coordinate[0], coordinate[1] + height))
        GeneratePieceCoordinates.count = (GeneratePieceCoordinates.count + 1) % (len(GeneratePieceCoordinates.pieces))
        return (nextPiece[0], nextPieceOffset, nextPiece[2])
if __name__ == "__main__":
    main()