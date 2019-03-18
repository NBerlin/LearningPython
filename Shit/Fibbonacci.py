first= 0
second=0
zero=True
limit=int(input())
for x in range(0,limit):
    newfirst=first+second
    print(newfirst)
    if zero:
        second=1
        zero=False
    else:
        second=first
        first=newfirst

numbers=[0,1]
for x in range(0,limit):
    numbers.append(numbers[x]+numbers[x+1])
for x in numbers:
    print(x)