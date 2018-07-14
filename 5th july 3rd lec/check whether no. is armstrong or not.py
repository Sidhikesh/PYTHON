#check whether the given no is armstrong or not      
x=int(input('enter the no'))
t=x
s=0
while(x!=0):
    x,rem=divmod(x,10)
    s=s+(rem**3)
if(s==t):
    print('Armstrong ')
else:print('no is not armstrong')
      
      
