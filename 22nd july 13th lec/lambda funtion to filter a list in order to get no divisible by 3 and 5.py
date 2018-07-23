#write a lambda funtion to filter a list in order to get no divisible by 3 and 5 only

l=[1,3,5,10,12,15,18,20,21,30]
no=[ x for x in filter(lambda a: True if a%3==0 and a%5==0 else False,l)]
print(no)
