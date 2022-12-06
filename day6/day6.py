def main():
    partTwo()

def partOne():
    with open('input.txt', 'r') as f:
        currentMap = {}
        items = []
        duplicates = True
        currentIndex = 0
        while True:
            currentIndex += 1
            nextChar = f.read(1)
            if not nextChar:
                break
            if nextChar not in currentMap:
                currentMap[nextChar] = 1
            else:
                currentMap[nextChar] += 1
            if len(items) >= 4:
                removedChar = items[0]
                items = items[1:]
                items.append(nextChar)
                currentMap[removedChar] -= 1
                print(items)
            else:
                items.append(nextChar)
                continue
            for item in items:
                if currentMap[item] > 1:
                    duplicates = True
                    break
                else:
                    duplicates = False
            if not duplicates:
                print(currentIndex)
                break
                

def partTwo():
    with open('input.txt', 'r') as f:
        currentMap = {}
        items = []
        duplicates = True
        currentIndex = 0
        while True:
            currentIndex += 1
            nextChar = f.read(1)
            if not nextChar:
                print(currentMap)
                print(items)
                break
            if nextChar not in currentMap:
                currentMap[nextChar] = 1
            else:
                currentMap[nextChar] += 1
            if len(items) >= 14:
                removedChar = items[0]
                items = items[1:]
                items.append(nextChar)
                currentMap[removedChar] -= 1
            else:
                items.append(nextChar)
                continue
            for item in items:
                if currentMap[item] > 1:
                    duplicates = True
                    break
                else:
                    duplicates = False
            if not duplicates:
                print(currentIndex)
                break


if __name__ == "__main__":
    main()