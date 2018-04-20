puzzle=265149
test=True
test2=True
n=1
y=0
while test:
    if n*n>puzzle:
        test=False
        puzzle=puzzle-(n*n)
        print(puzzle)
        print(y)
        while test2:
            if puzzle-n>0:


                n=2
            else:
                puzzle=puzzle+n
    n=n+2
    y=y+1