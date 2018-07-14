x=input('enter a sentence')
lower=x.lower()
y=input('enter a word')

s=lower.split()
list=[]
for each in s:
    if (each==y):
        list.append(y)
count=len(list)
print(count)
        
