def main():
    partTwo()

def partOne():
    originalList = []
    with open("input.txt") as f:
        for line in f:
            originalList.append(int(line.strip()))
    
    linkedList = []
    for item in originalList:
        linkedList.append(Node(item))
    
    for i in range(-1, len(linkedList) - 1):
        linkedList[i].link(nextNode=linkedList[i+1], parent=linkedList[i - 1])
    
    # test linked list
    # origin = linkedList[0]
    # 
    # while not nextNode is origin:
    #     print("Current node is", nextNode.current)
    #     nextNode = nextNode.parent

    # nextNode = linkedList[0].nextNode
    # while nextNode != linkedList[0]:
    #     print("Original Current: %d, next is %d" %(nextNode.current, nextNode.nextNode.current))
    #     nextNode = nextNode.nextNode

    for i, item in enumerate(linkedList):
        bubbleAmount = item.current
        originalParent = item.parent
        originalChild = item.nextNode
        originalParent.nextNode = originalChild 
        originalChild.parent = originalParent
        if bubbleAmount > 0:
            nextNode = originalChild
            while bubbleAmount != 0:
                bubbleAmount -= 1
                nextNode = nextNode.nextNode
            newParent = nextNode.parent
            nextNode.parent = item
            item.nextNode = nextNode
            item.parent = newParent
            newParent.nextNode = item
        else:
            nextNode = originalParent
            while bubbleAmount != 0:
                bubbleAmount += 1
                nextNode = nextNode.parent
            newChild = nextNode.nextNode
            nextNode.nextNode = item
            item.parent = nextNode
            item.nextNode = newChild
            newChild.parent = item
    
    nextNode = linkedList[0]
    while nextNode.current != 0:
        nextNode = nextNode.nextNode
    
    total = 0
    seen = 0
    counter = 0
    while seen < 3:
        nextNode = nextNode.nextNode
        counter += 1
        if counter == 1000:
            print("value is %d" %(nextNode.current))
            total += nextNode.current
            counter = 0 
            seen += 1
    print(total)
        

class Node:
    def __init__(self, current, nextNode=None, parent=None):
        self.current = current
        self.nextNode = nextNode
        self.parent = parent

    def link(self, nextNode, parent):
        self.nextNode = nextNode
        self.parent = parent

def partTwo():
    originalList = []
    with open("input.txt") as f:
        for line in f:
            originalList.append(int(line.strip()) * 811589153)
    
    linkedList = []
    for item in originalList:
        linkedList.append(Node(item))
    
    for i in range(-1, len(linkedList) - 1):
        linkedList[i].link(nextNode=linkedList[i+1], parent=linkedList[i - 1])

    for _ in range(10):
        for i, item in enumerate(linkedList):
            bubbleAmount = item.current % (len(linkedList) - 1)
            originalParent = item.parent
            originalChild = item.nextNode
            originalParent.nextNode = originalChild 
            originalChild.parent = originalParent
            if bubbleAmount > 0:
                nextNode = originalChild
                while bubbleAmount != 0:
                    bubbleAmount -= 1
                    nextNode = nextNode.nextNode
                newParent = nextNode.parent
                nextNode.parent = item
                item.nextNode = nextNode
                item.parent = newParent
                newParent.nextNode = item
            else:
                nextNode = originalParent
                while bubbleAmount != 0:
                    bubbleAmount += 1
                    nextNode = nextNode.parent
                newChild = nextNode.nextNode
                nextNode.nextNode = item
                item.parent = nextNode
                item.nextNode = newChild
                newChild.parent = item
    
    nextNode = linkedList[0]
    while nextNode.current != 0:
        nextNode = nextNode.nextNode
    
    total = 0
    seen = 0
    counter = 0
    while seen < 3:
        nextNode = nextNode.nextNode
        counter += 1
        if counter == 1000:
            print("value is %d" %(nextNode.current))
            total += nextNode.current
            counter = 0 
            seen += 1
    
    print(total)

if __name__ == "__main__":
    main()