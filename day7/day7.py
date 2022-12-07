from collections import deque

def main():
    partTwo()

def getBranch(tokenized):
    global currentSubTree
    if tokenized[2] == "..":
        currentSubTree = currentSubTree.parent
    elif currentSubTree is None:
        currentSubTree = Node(tokenized[2], 0)
    else:
        currentSubTree = currentSubTree.getChild(tokenized[2])

currentSubTree = None

def doNothing(tokenized):
    pass

visited = {}

validCommands = {
    "cd": getBranch,
    "ls": doNothing
}

def partOne():
    buildTree()
    frontier = deque()
    frontier.append(currentSubTree)
    isLarger = 0
    while frontier:
        nextNode = frontier.popleft()
        if nextNode.getSize() < 100000 and nextNode.children:
            isLarger+=nextNode.getSize()
        nodeChildren = nextNode.children
        for nodeChild in nodeChildren:
            if not visited[nodeChild]:
                frontier.append(nodeChild)
                visited[nodeChild] = True
    print(isLarger)
    pass

def partTwo():
    buildTree()
    frontier = deque()
    frontier.append(currentSubTree)
    smallest = 70000000
    requiredSpace = 30000000 - (70000000 - currentSubTree.getSize())
    print(requiredSpace)
    while frontier:
        nextNode = frontier.popleft()
        if nextNode.children and nextNode.getSize() < smallest and nextNode.getSize() >= requiredSpace:
            smallest = nextNode.getSize()
        elif not nextNode.children:
            continue
        nodeChildren = nextNode.children
        for nodeChild in nodeChildren:
            if not visited[nodeChild]:
                frontier.append(nodeChild)
                visited[nodeChild] = True
    print(smallest)


def buildTree():
    global currentSubTree
    with open("input.txt") as f:
        for line in f:
            tokenized = line.strip("\n").split(" ")
            if tokenized[0] == "$":
                command = validCommands[tokenized[1]]

                command(tokenized)
            else:
                size = 0
                if tokenized[0] != "dir":
                    size = int(tokenized[0])
                newChild = Node(tokenized[1], size, currentSubTree)
                currentSubTree.addChildDirect(newChild)
                visited[newChild] = False
        
        # traverse to root node
        while currentSubTree.parent is not None:
            currentSubTree = currentSubTree.parent
class Node():
    def __init__(self, name, size=0, parent=None):
        self.updated = False
        self.name = name
        self.children = []
        self.size = size
        self.parent = parent
    
    def getSize(self):
        if not self.updated:
            for child in self.children:
                self.size += child.getSize()
            self.updated = True
        return self.size

    def addChild(self, child):
        self.children.append(child)
        self.updated = False
        parent = self.parent
        while True:
            parent.updated = False
            parent = parent.parent
            if parent is None:
                break
    
    def addChildDirect(self, child):
        # Note: saves runtime when not computing size when building tree. Updates to tree must
        # use `setChild(child)`
        self.children.append(child)
        self.updated = False
    
    def getChild(self, childName):
        for child in self.children:
            if child.name == childName:
                return child
        return None


if __name__ == "__main__":
    main()