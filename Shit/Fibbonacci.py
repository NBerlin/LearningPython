
limit=int(input())
numbers=[0,1]
for x in range(0,limit):
    numbers.append(numbers[x]+numbers[x+1])
for x in numbers:
    print(x)