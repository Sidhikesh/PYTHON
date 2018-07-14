word=input('enter a string')
l=word.split()
x1=[]
x2=[]
for each in l:
    if each not in x1:
        print(each,':',l.count(each))
        x1.append(each)
print(x1)
x1.sort()
print(x1)
for each in x1 :
        x2.append(l.count(each))
print(x2)

    
    

