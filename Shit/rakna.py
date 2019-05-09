import collections
testlist=[]
class Node:
    def __init__(self,value):
        self.children = []
        self.value=value
    def addChild(self,c,c2):
        self.children.append(c[0])
        self.children.append(c2[0])
    def getChildren(self):
        return self.children

def makePair(first,second):
    newNode=[Node(first[1]+second[1]),first[1]+second[1]]
    newNode[0].addChild(first,second)
    listInsert(newNode)
def listInsert(item):
    i=0
    for object in frequency:
        if object[1]>item[1]:
            break
        i+=1
    frequency.insert(i,item)
    testlist.append(item)
    


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
while len(frequency)!=1:
    test=frequency.pop(0)
    test2=frequency.pop(0)
    makePair(test,test2)

testlist.reverse()
for item in testlist:
    temp=item[0].getChildren()
    printlist=[]
    for item2 in temp:
        if type(item2)==Node:
            printlist.append(item2.value)
        else:
            printlist.append(item2)
            
    print(item[1],printlist)








