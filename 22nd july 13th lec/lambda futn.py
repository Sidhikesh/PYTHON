#lambda funtion
'''
l1=[4,5,6]
l2=[3,5,8]
l=[x for x in map(lambda m,n:m+n,l1,l2)]
print(l)'''


'''l1=[4,5,6]
l2=[3,5,8]
#a=int(input('enter a no'))
#b=int(input('enter a no'))
l=[ x for x in map(lambda a,b: a if a>b else b,l1,l2) ]
#print(l[0](a,b))
print(l)'''




l1=[4,5,6]
l2=[2,8,8]
l=[ x for x in map(lambda a,b: (a,b) if a%b==0 else (-1,-2),l1,l2) ]
print(l)




