input = open("Day2.txt","r")
puzzle =input.readlines()
totalsum=0
for s in puzzle:
    s=s[:-1]
    line=s.split("\t")
    print(line)
    for n in line:
            n=int(n)
            for y in line:
                y=int(y)
                if n%y==0 and n!=y:
                    totalsum+=n/y

print(totalsum)