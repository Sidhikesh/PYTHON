x=int(input('enter a no'))
for i in range (2,x):
        if(x%i==0):
            break
if(i==x-1):
        print('it is a prime no')
else:print('it is not a prime no.')
