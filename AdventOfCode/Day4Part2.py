input = open("day4.txt","r")
puzzle =input.readlines()
for s in puzzle:


    line=s.split()
    c=set(line)
    for n in c:
        newlist = [list(item) for item in n]
        for y in c:
            newlist2 = [list(item2) for item2 in y]
            if set(str([newlist2,newlist]))==len(y):
                print("false")



