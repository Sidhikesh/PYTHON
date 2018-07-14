temp=word=input('enter a string')
l=list(word)
l.reverse()
word=''.join(l)
if temp==word:
    print('it is palindrome')
else:
    print('not a palindrome')
