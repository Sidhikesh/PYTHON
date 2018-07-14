x=int(input('enter 1st no.'))
y=int(input('enter 2nd no.'))
a,b=x,y
while(x!=y):
    if(x>y):
        x-=y
    else:
        y-=x
gcd=x
lcm=a*b/x
print('gcd',gcd,'lcm',lcm)
