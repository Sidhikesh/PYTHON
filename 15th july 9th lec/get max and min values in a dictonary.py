d={'phy': 67, 'maths': 69, 'chm': 35, 'hist': 9}
list1=[]
mini=0

for each in d.values():
    list1.append(each)
word=list1[0]

for i in range(len(list1)):
    if(word > list1[i]):
        mini=list1[i]
print(mini)
        


