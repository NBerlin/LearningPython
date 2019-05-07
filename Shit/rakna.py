import collections
class Node:
    def __init__(self,value):
        self.children = []
        self.value=value
    def addChild(self,c,c2):
        self.children.append(c[1])
        self.children.append(c2[1])
    def getChildren(self):
        return [self.children]
def getChildren(n):
    if type(n)==Node:
        ch= n.getChildren()
        for item in ch:
            item.getChildren()
    return n

def findLowest(l):
    return frequency.pop()

def makePair(first,second):
    newNode=[Node(first[1]+second[1]),first[1]+second[1]]
    newNode[0].addChild(first,second)
    listInsert(newNode)
def listInsert(item):
    i=0
    for object in frequency:
        if object[1]>item[1]:
            frequency.insert(i,item)
            break
        i+=1
    frequency.append(item)


file = open("alice.txt",mode='r')
frequency = {}
nbrOfLines=0
for line in file:
    nbrOfLines+=1
    for character in line:
        if not character in frequency:
            frequency[character] = 0
        frequency[character] += 1
frequency['NL']=nbrOfLines
frequency['\x1a']=0
frequency = sorted(frequency.items(), key=lambda x: x[1])
frequency.pop(0)
while len(frequency)!=2:
    test=frequency.pop(0)
    test2=frequency.pop(0)
    makePair(test,test2)

makePair(frequency.pop(0),frequency.pop(0))
getChildren(frequency[0][0])







