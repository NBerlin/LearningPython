input = open("24.txt","r")
puzzle =input.readlines()
totalsum=0
for s in puzzle:
    line=s.split("\t")
    biggest =0
    smallest=9999
    for n in line:
        if n.find("\n")==-1:
            n=int(n)
            if n<smallest:
                if (smallest > biggest) and (smallest!=9999):
                    biggest=smallest
                smallest=n
            elif n>biggest:
                biggest=n

        else:
            a,b=n.split("\n")
            a=int(a)
            if a<smallest:
                if smallest > biggest:
                    biggest=smallest
                smallest=a
            elif a>biggest:
                biggest=a
    totalsum=totalsum+(biggest-smallest)
    print(biggest,smallest)
print(totalsum)