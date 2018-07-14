a=[]

for i in range (0,5):
    x=input('enter string')
    a.append(x)
    print (len(a[i]))
print(a)
length=len(a[0])
pos=0
for j in range (0,len(a)):
    if(len(a[j]) > length):
        pos=j        
print('Largest string is',a[pos])
