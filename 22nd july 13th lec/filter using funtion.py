#filter using funtion
def even(a):
    if a%2==0:
        return True
    else:
        return False
l1=[2,3,4,6,7,3]
l=[x for x in filter(even,l1)]
print(l)
