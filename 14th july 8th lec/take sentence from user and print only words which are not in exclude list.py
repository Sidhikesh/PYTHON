exclude=['is','am','are','of','as','on','a']
x=input('enter a sentence')
lower=x.lower()
s=lower.split()
list=[]
for each in s:
    if each not in exclude:
        list.append(each)
sentence=' '.join(list)
print(sentence)
        
