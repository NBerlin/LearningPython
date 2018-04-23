def prime(number):
    oldnum = number
    factor = 1
    while number > 1:
        factor += 1
        if number % factor == 0:
            if 1 < factor < oldnum:
                return False
            number //= factor
    return True
for x in range(1,int(input())):
    print(prime(x))