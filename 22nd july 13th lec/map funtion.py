#take 2 input and calulate sum

'''def sum(a,b):
    return a+b
l1=[1,2,3]
l2=[4,5,6]
map(sum,l1,l2)


L=[x for x in map(sum,l1,l2)]
print(L)'''

#take 2 input and calulate sqaure by adding2

'''def square_plus(a):
    return (a**2)+2
l1=[1,2,3]
l2=[4,5,6]



L=[x for x in map(square_plus,l1)]
print(L)'''


#take 3 input and calulate sum

'''def sum(a,b,c):
    return a+b+c
s=[2,3,4]
y=[5,6,7]
z=[7,8,9]


l=[x for x in map(sum,s,y,z)]
print(l)'''


#take 5 input and calculate sum, total, avg
def sum_avg(a,b,c,d,e):
    total=a+b+c+d+e
    avg=total/5.0
    return total,avg
l1=[1,2,3]
l2=[4,5,6]
l3=[2,5,7]
l4=[6,9,8]
l5=[1,5,3]
d={total:avg for total,avg in map(sum_avg,l1,l2,l3,l4,l5)}
print(d)
