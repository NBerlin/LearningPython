import collections
testlist = []


class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def addChild(self, c, c2):
        self.children.append(c[0])
        self.children.append(c2[0])

    def getChildren(self):
        return self.children


def makePair(first, second):
    newNode = [Node(first[1]+second[1]), first[1]+second[1]]
    newNode[0].addChild(first, second)
    listInsert(newNode)


def listInsert(item):
    i = 0
    for object in frequency:
        if object[1] > item[1]:
            break
        i += 1
    frequency.insert(i, item)
    testlist.append(item)


encodedlist={(',', '100100'),
 ('`', '1001010'),
 ('!', '111001011'),
 ('\n', '01000'),
 ('.', '0101110'),
 ('*', '0101000010'),
 (':', '010111110'),
 (']', '01010001111010'),
 ('_', '01010001111100'),
 ('[', '010100011111010'),
 ('-', '11000010'),
 ('"', '11100101001'),
 (';', '1110010000'),
 ('NL','01001'),
 ('?', '1110010011'),
 (')', '111001001010'),
 ('(', '111001001011'),
 (' ', '00'),
 ('a', '0111'),
 ('b', '1100000'),
 ('c', '100001'),
 ('d', '10011'),
 ('e', '1101'),
 ('f', '010101'),
 ('g', '101000'),
 ('h', '11111'),
 ('i', '11101'),
 ('j', '0101000110'),
 ('k', '0101001'),
 ('l', '10001'),
 ('m', '010110'),
 ('n', '11110'),
 ('o', '0110'),
 ('p', '1100010'),
 ('q', '010100010'),
 ('r', '10101'),
 ('s', '11001'),
 ('t', '1011'),
 ('u', '111000'),
 ('v', '11000110'),
 ('w', '101001'),
 ('x', '100101111'),
 ('y', '100000'),
 ('z', '1001011001'),
 ('A', '10010110'),
 ('B', '11000011010'),
 ('C', '100101110'),
 ('D', '1100001111'),
 ('E', '1100001110'),
 ('F', '1001011000'),
 ('G', '1001011011'),
 ('H', '010100010'),
 ('I', '11000111'),
 ('J', '0101000111111'),
 ('K', '1001011010'),
 ('L', '11100100100'),
 ('M', '1110010001'),
 ('N', '010100000'),
 ('O', '1100001100'),
 ('P', '0101000011'),
 ('Q', '11000011011'),
 ('R', '0101000111'),
 ('S', '1110010101'),
 ('T', '01011110'),
 ('U', '0101000110'),
 ('V', '01010001110'),
 ('W', '010111111'),
 ('X', '0101000111100'),
 ('Y', '11100101000'),
 ('Z', '01010001111101'),
 ('2', '010100011110100'),
 ('9', '010100011110101'),
 }


file = open("alice.txt", mode='r')
frequency = {}
nbrOfLines = 0
for line in file:
    nbrOfLines += 1
    for character in line:
        if not character in frequency:
            frequency[character] = 0
        frequency[character] += 1
frequency['NL'] = nbrOfLines
frequency['\x1a'] = 0
ones=0
zeroes=0
for item in encodedlist:
    tempZero=0
    tempOne=0
    numberList=list(item[1])
    for number in numberList:
        if int(number)==1:
            
            tempOne+=1
        else:
            tempZero+=1
    ones+=tempOne*frequency[item[0]]
    zeroes+=tempZero*frequency[item[0]]
print("Number of '1' in encoded message:",ones,"\nNumber of '0' in encoded message:",zeroes
    ,"\nRatio between '1' and '0':",round(ones/zeroes,2))

sum=0
for item in encodedlist:
    sum+=frequency[item[0]]*len(item[1])
print("Amount of bits encoded with Huffman:",
sum,"\nAmount of bits encoded normally:",152089*8,
"\nRatio between Huffman encoding and regular 8 bit: ", round(sum/(152089*8),2),
"\nAverage bitlength per character",round(sum/152089,2))   


frequency = sorted(frequency.items(), key=lambda x: x[1])
frequency.pop(0)
frequency.reverse()

while len(frequency) != 1:
    test = frequency.pop(0)
    test2 = frequency.pop(0)
    makePair(test, test2)

testlist.reverse()
for item in testlist:
    temp = item[0].getChildren()
    printlist = []
    for item2 in temp:
        if type(item2) == Node:
            printlist.append(item2.value)
        else:
            printlist.append(item2)


