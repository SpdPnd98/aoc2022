def main():
    partTwo()

def partOne():
    with open("input.txt") as f:
        head = Head()
        tail = Tail()
        head.tieTail(tail)
        for line in f:
            direction, steps = line.strip("\n").split(" ")
            steps = int(steps)
            Head.goTo(direction, steps, head)
        
        print(len(tail.visited))

def partTwo():
    with open("input.txt") as f:
        head = Head()
        body = Tail()
        tail = body
        for i in range (0, 8):
            body = Body(body, str(8 - i))
        head.tieTail(body)
        for line in f:
            direction, steps = line.strip("\n").split(" ")
            steps = int(steps)
            Head.goTo(direction, steps, head)
        print(len(tail.visited))
        # print(tail.visited)
        # head.viewPos()

direction = {
    'R': (1,  0),
    'L': (-1, 0),
    'U': (0,  1),
    'D': (0, -1)
}

class Head:

    @staticmethod
    def goTo(dir, steps, head):
        global direction
        goDirSteps = direction[dir]
        # print(dir + " " + str(steps))
        for i in range(0, steps):
            # print("item " + str(i))
            head.move(goDirSteps[0], goDirSteps[1])
    
    def __init__(self):
        self.currentX = 0
        self.currentY = 0
    
    def move(self, x, y):
        self.prevX = self.currentX
        self.prevY = self.currentY
        self.currentX += x
        self.currentY += y
        self.tail.trail(self)

    def tieTail(self, tail):
        self.tail = tail

    def viewPos(self):
        tailPos = self.tail.viewPos()
        print(str((self.currentX, self.currentY)) + " " + tailPos)

class Tail:
    def __init__(self):
        self.currentX = 0
        self.currentY = 0
        self.visited = set()
        self.visited.add((self.currentX, self.currentY))
    
    def trail(self, head):
        deltaX = head.currentX - self.currentX
        deltaY = head.currentY - self.currentY

        if abs(deltaX) >= 2 or abs(deltaY) >= 2:
            xDir = 1 if deltaX > 0 else 0 if deltaX == 0 else -1
            yDir = 1 if deltaY > 0 else 0 if deltaY == 0 else -1
            self.currentX += xDir
            self.currentY += yDir
            self.visited.add((self.currentX, self.currentY))

    def viewPos(self):
        return str((self.currentX, self.currentY))

class Body:
    def __init__(self, tail, qualifier):
        self.currentX = 0
        self.currentY = 0
        self.tail = tail
        self.qualifier = qualifier
    
    def trail(self, head):
        # print(self.qualifier + " " + str(head.prevX))
        deltaX = head.currentX - self.currentX
        deltaY = head.currentY - self.currentY

        if abs(deltaX) >= 2 or abs(deltaY) >= 2:
            xDir = 1 if deltaX > 0 else 0 if deltaX == 0 else -1
            yDir = 1 if deltaY > 0 else 0 if deltaY == 0 else -1
            self.currentX += xDir
            self.currentY += yDir
            self.tail.trail(self)
    
    def viewPos(self):
        tailPos = self.tail.viewPos()
        return str(str((self.currentX, self.currentY)) + " " + tailPos)

if __name__ == "__main__":
    main()