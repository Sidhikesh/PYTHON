no=int(input('enter the no'))
count=0
if(no==0):
    print('count is 1')
while(no!=0):
        count=count+1
        no=no//10
print(count)
