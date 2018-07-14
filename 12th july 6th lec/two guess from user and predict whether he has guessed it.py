from random import randint
r=print(randint(1,10))
g1=int(input('Enter your 1st guess'))
g2=int(input('Enter your 2st guess'))
if(g1==r or g2==r):
    print('you have won')
for i in range (1,5):
    if(g1>0 and g2>0):
        print('try one more time')
    elif(g1<g2 and g2<10):
        print('try one more time')
    elif(g1<g2 or g2>10):
        print('try one more time')
print('end of program')
