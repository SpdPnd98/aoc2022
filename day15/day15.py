def main():
    # partOne(y=2000000)
    print(partTwo(maxDir=4000000))

def combineRanges(x1, x2, x3, x4):
    if x3 <= x1 and x4 >= x2:
        # print("case 3", (x1, x2, x3, x4))
        return [(x3, x4)]
    elif x3 >= x1 and x3 < x2 and x4 >= x2:
        # print("case 1", (x1, x2, x3, x4))
        return [(x1, x4)]
    elif x4 > x1 and x4 <= x2 and x3 <= x1:
        # print("case 2", (x1, x2, x3, x4))
        return [(x3, x2)]
    elif x3 >= x1 and x4 <= x2:
        # print("case 4", (x1, x2, x3, x4))
        return [(x1, x2)]
    elif x4 == x1:
        # print("case 5", (x1, x2, x3, x4))
        return [(x3, x2)]
    elif x3 == x2:
        # print("case 6", (x1, x2, x3, x4))
        return [(x1, x4)]
    else:
        # print("no overlap ", (x1, x2, x3, x4))
        return [(x1, x2), (x3, x4)]
    
def within(x1, x2, targetX):
    return targetX >= x1 and targetX <= x2

def partOne(filename="input.txt", y=10):
    sensors, _ = generateSensorBeacons(filename)
    count, _ = getTotalCounts(sensors, y)
    print(count)
    return count

def getTotalCounts(sensors, y):
    xRanges = set()
    for index in sensors:
        sensor = sensors[index]
        delta = sensor.mDistance - abs(sensor.y - y)
        if delta < 0:
            continue
        newRange = (sensor.x - delta, sensor.x + delta)
        # print((sensor.x, sensor.y), "generated", newRange)
        if len(xRanges) == 0:
            xRanges.add(newRange)
        else:
            temp = set()
            while len(xRanges) > 0:
                xRange = xRanges.pop()
                items = combineRanges(xRange[0], xRange[1], newRange[0], newRange[1])
                if len(items) == 2:
                    temp.add(items[0])
                else:
                    newRange = items[0]
                # print(items)
            # print(temp, newRange)
            temp.add(newRange)
            xRanges = temp
            
    count = 0
    for xRange in xRanges:
        count += xRange[1] - xRange[0] 

    return count, xRanges

def trimRanges(minX, maxX, ranges):
    newRanges = set()
    for currRange in ranges:
        if currRange[1] >= minX or currRange[0] <= maxX:
            newRanges.add((max(currRange[0], minX), min(currRange[1], maxX)))
    return newRanges

def partTwo(filename="input.txt", maxDir=20):
    sensors, _ = generateSensorBeacons(filename)
    for y in range(0, maxDir): # x and y share the same parameter
        _, countRanges = getTotalCounts(sensors, y)
        xRangesTrimmed = trimRanges(0, maxDir, countRanges)
        if len(xRangesTrimmed) == 2:
            itemOne = xRangesTrimmed.pop()
            itemTwo = xRangesTrimmed.pop()
            if itemOne[1] < itemTwo[0]:
                print(set([itemOne, itemTwo])) # dun care first
                return set([itemOne, itemTwo]), y
            else:
                print(set([itemOne, itemTwo])) # dun care first
                return set([itemOne, itemTwo]), y
        elif len(xRangesTrimmed) > 2:
            print("Something happened", (xRangesTrimmed, y))
            return xRangesTrimmed, y
        else:
            item = xRangesTrimmed.pop()
            if item != (0, maxDir):
                print("check if there is something at ", y, xRangesTrimmed)
                return set([item]), y
            else:
                print("No beacons found at", y)

def generateSensorBeacons(filename="input.txt"):
    beaconSet = set()
    sensorSet = {}
    with open(filename) as f:
        for line in f:
            sentence = line.split(" ")
            sensorPos = parseXY(sentence[2], sentence[3])
            beaconPos = parseXY(sentence[-2], sentence[-1])
            beaconSet.add(beaconPos)
            mDistance = abs(sensorPos[0] - beaconPos[0]) + abs(sensorPos[1] - beaconPos[1])
            sensorSet[sensorPos] = Sensor(sensorPos[0], sensorPos[1], mDistance)        
    
    return sensorSet, beaconSet

def parseXY(x, y):
    intX = int(x[:-1].split("=")[1])
    intY = int(y[:-1].split("=")[1])
    return intX, intY

class Sensor:
    def __init__(self, x, y, mDistance):
        self.x = x
        self.y = y
        self.mDistance = mDistance

    def touched(self, x, y):
        return abs(self.x - x) + abs(self.y - y) <= self.mDistance

if __name__ == "__main__":
    main()