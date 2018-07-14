l1=[45,65,78,23]
l2=[45,65,77,22]
for  x  in l1:
    if x not in  l2:
        print(x)
for x in l2:
    if x not in l1:
        print(x)
    


