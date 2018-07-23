a={'a':10,'b':20,'c':30}
b={'c':10,'f':20,'g':30}
d={}
for each in a:
    if each in b:
        d.setdefault(each,a[each]+b[each])
    else:
            d.setdefault(each,a[each])
for each in b:
    if each not in d:
        d.setdefault(each,b[each])
print(d)
        
