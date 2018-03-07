#öppnar/skapar en text.txt fil och är i append mode.
file=open("test.txt","a")
while 1==1:

    myName = input("Vad heter du? ")
    if myName=="stop":
        break
    if myName=="print":
        file.close()
        file=open("test.txt","r")
        print(file.read())
        break
    myDate = input("Vilket datum jobbade du? ")
    myTime = input("Vilken tid jobbade du? ")
    file.write(myName+" "+myDate+" "+myTime+"\n")
