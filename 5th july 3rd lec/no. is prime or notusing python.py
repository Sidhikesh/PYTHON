x=int(input('enter a no.'))
for i in range (2,x):
    if(x%i==0):
        print('no is not  prime')
        break
if(i==x-1):
        print('no is  prime')
