#compresion forcreating dictionary
#create a dictionary containing cube of no. which is divisible by 2
a=int(input('enter a value'))
b=int(input('enter a value'))
D={}

D={x:x**3 for x in range (a,b+1) if x%2==0}
print(D)
