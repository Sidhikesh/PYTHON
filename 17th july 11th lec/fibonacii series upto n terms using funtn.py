def fibo (no):
    a=0
    b=1
    print(a,b)
    for i in range (1,no-1):
        c=a+b
        print(c)
        a,b=b,c
    return()
no=int(input('enter a no'))
fibo(no)
