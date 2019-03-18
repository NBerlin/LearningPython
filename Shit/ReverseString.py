string = str(input())
first = True
for char in string:
    if first:
       newString=char
       first=False;
    else:
        newString = char + newString

print(newString)
output=""
for char in string:
    output=char + output

print(output)

def sickRekursion(s):
    if s=="":
        return ""
    return sickRekursion(s[1:])+s[0]
print(sickRekursion(string))