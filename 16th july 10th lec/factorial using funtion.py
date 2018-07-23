def facto (no):
    fact=1
    for i in range (1,no+1):
        fact=fact*i
    return fact
num=int(input('enter a no'))
print('factorial is',facto(num))
