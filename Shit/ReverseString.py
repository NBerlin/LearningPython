string = str(input())
first = True
for char in string:
    if first:
       newString=char
       first=False;
    else:
        newString = char + newString

print(newString)