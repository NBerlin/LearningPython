first= 0
second=0
zero=True
for x in range(0,int(input())):
    newfirst=first+second
    print(newfirst)
    if zero:
        second=1
        zero=False
    else:
        second=first
        first=newfirst