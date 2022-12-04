def main():
    partTwo()

def partOne():
    with open("input.txt") as f:
        numContains = 0
        for line in f:
            r1, r2 = line.split(",")
            r1a, r1b = r1.split("-")
            r2a, r2b = r2.split("-")
            if (int(r1a) <= int(r2a) and int(r1b) >= int(r2b)) or (int(r1a) >= int(r2a) and int(r1b) <= int(r2b)):
                numContains += 1
        
        print(numContains)


def partTwo():
    with open("input.txt") as f:
        numContains = 0
        for line in f:
            r1, r2 = line.split(",")
            r1a, r1b = r1.split("-")
            r2a, r2b = r2.split("-")
            if within(r1a, r1b, r2a, r2b) or intersect(r1a, r1b, r2a, r2b):
                numContains += 1
        
        print(numContains)

def within(r1a, r1b, r2a, r2b):
    return (int(r1a) <= int(r2a) and int(r1b) >= int(r2b)) or (int(r1a) >= int(r2a) and int(r1b) <= int(r2b))

def intersect(r1a, r1b, r2a, r2b):
    return (int(r1a) <= int(r2b) and int(r1a) >= int(r2a)) or (int(r2a) <= int(r1b) and int(r2a) >= int(r1a))

if __name__ == "__main__":
    main()