def main():
    partTwo()

def partOne():
    trees = constructMatrix()
    viewableTree = 2* (len(trees) + len(trees[0]) - 2)
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            # check left
            compares = 0
            for s in range(0, i):
                compares = max(trees[s][j], compares)
            if larger(trees[i][j], compares):
                viewableTree += 1
                continue
            # check right
            compares = 0
            for s in range(i+1, len(trees)):
                compares = max(trees[s][j], compares)
            if larger(trees[i][j], compares):
                viewableTree += 1
                continue
            # check up
            compares = 0
            for s in range(0, j):
                compares = max(trees[i][s], compares)
            if larger(trees[i][j], compares):
                viewableTree += 1
                continue
            # check down
            compares = 0
            for s in range(j+1, len(trees)):
                compares = max(trees[i][s], compares)
            if larger(trees[i][j], compares):
                viewableTree += 1
                continue
    print(viewableTree)

def partTwo():
    trees = constructMatrix()
    score = 1
    highestScore = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            # check left
            treesViewable = 0
            for s in range(i-1, -1, -1):
                treesViewable += 1
                if(trees[i][j] <= trees[s][j]):
                    break
            score *= treesViewable
            # check right
            treesViewable = 0
            for s in range(i+1, len(trees)):
                treesViewable += 1
                if(trees[i][j] <= trees[s][j]):
                    break
            score *= treesViewable
            # check up
            treesViewable = 0
            for s in range(j-1, -1, -1):
                treesViewable += 1
                if(trees[i][j] <= trees[i][s]):
                    break
            score *= treesViewable
            # check down
            treesViewable = 0
            for s in range(j+1, len(trees)):
                treesViewable += 1
                if(trees[i][j] <= trees[i][s]):
                    break
            score *= treesViewable
            highestScore = max(score, highestScore)
            score = 1
    print(highestScore)

def larger(item, value):
    return item > value

def constructMatrix():
    matrix = []
    with open("input.txt") as f:
        row = []
        while True:
            nextChar = f.read(1)
            if nextChar == "\n":
                matrix.append(row)
                row = []
            elif nextChar == "":
                break
            else:
                row.append(int(nextChar))
    return matrix



if __name__ == "__main__":
    main()