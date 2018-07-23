
def palindrome(num):
    sum1=0
    while num!=0:
       rem=num%10
       sum1=sum1*10+rem
       num=num//10
    return sum1

no=int(input('enter a no'))

x=palindrome(no)
if no==x:
    print('palindrome')
else:print('it is not palindrome')
