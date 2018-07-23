#count programs using dictionary
#count the no of keys in a dictionary
'''word=input('enter a string')
l=word.split()
x1={}
for each in l:
        z=x1.setdefault(each,l.count(each))
print(z)
print(x1)'''
         


'''word=input('enter a string')
l=word.split()
x1={}
for each in l:
        z=x1.setdefault(each,l.count(each))
for each in x1.keys():
        print('for the word',each ,' the value is', x1.get(each))
        
print(z)
print(x1)'''


word=input('enter a string')
l=word.split()
x1={}
for each in l:
      z=x1.setdefault(each,l.count(each))
for k,v in x1.items():
        print('for the word',k ,' the value is', v)
        
print(x1)


                                                                   
