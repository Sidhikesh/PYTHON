'''
   * 
  * * 
 * * * 
* * * * 
 * * *
  * *
   *
for i in range(5):
    for j in range (4-i):
        print('',end=' ')
    for j in range (i):
        print('*',end=' ')
    print()
for i in range (3,0,-1):
    for j in range (3-i):
        print(' ',end='')
    for j in range (i):
        print(' *',end='')
    print()
-------------------------------------------------------------


ABCDE
ABCD
ABC
AB
A

for i in range (5):
    for j in range (5-i):
        print(chr(65+j),end='')
    print()

--------------------------------------------------------------
    

    P 
   P Q 
  P Q R 
 P Q R S
for i in range (5):
    for j in range (5-i):
        print('',end=' ')
    for j in range (i):
        print(chr(j+80),end=' ')
    print()
'''

-------------------------------------------------------------

    A
   ab
  ABC
 abcd
for i in range(5):
    for j in range (5-i):
        print('',end=' ')
    for j in range (i):
        if i%2!=0:
            print(chr(j+65),end='')
        else: print(chr(j+97),end='')
    print()











    
    
