input = open("Day4.txt","r")
puzzle =input.readlines()
numberOfValidLines =0
for s in puzzle:
    print(s)
    line=s.split()
    c=set(line)
    if len(c)==len(line):
        numberOfValidLines+=1

print(len(puzzle))
print(numberOfValidLines)
