input = open("Day5.txt","r")
input= input.readlines()
input=[i.split('\n', 1)[0] for i in input]
input = list(map(int, input))
x=0
jumps=0
while x<len(input):
    temp=x
    x=x+input[x]
    input[temp]+=1
    print(x)
    jumps+=1
print(jumps)