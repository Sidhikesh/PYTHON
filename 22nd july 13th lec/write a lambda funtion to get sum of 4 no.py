'''def sum_avg(a,b,c,d):
    total=a+b+c+d
    return total
l1=[1,2,3]
l2=[4,5,6]
l3=[2,5,7]
l4=[6,9,8]

d=[total for total in map(sum_avg,l1,l2,l3,l4)]
print(d)'''



l1=[1,2,3]
l2=[4,5,6]
l3=[2,5,7]
l4=[6,9,8]

d=[x for x in map(lambda a,b,c,d:a+b+c+d,l1,l2,l3,l4)]
print(d)
