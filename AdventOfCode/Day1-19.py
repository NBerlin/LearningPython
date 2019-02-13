
ans=0
myset={0}
mylist=[0]
run=True
while run:

    puzzle = open("day1")
    for item in puzzle:

        size=len(myset)
        ans=int(item)+ans
        myset.add(ans)
        mylist.append(ans)
        if(len(myset)==size):
            print(ans)
            run=False
            break
