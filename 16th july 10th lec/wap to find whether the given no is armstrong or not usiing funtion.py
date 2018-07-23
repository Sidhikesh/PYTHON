def armstrong (no):
    temp=no
    sum=0
    while(no!=0):
        no,rem=divmod(no,10)
        sum+=(rem**3)
    if(sum==temp):
        print('armstrong')
    else:print('it is not armstrong')
    return()

x=int(input('enter the no'))
armstrong(x)
