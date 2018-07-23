#wap to tell whether it is holiday or not
holiday=(5,16,27)
x=int(input('enter a date'))
for i in  range (1,31):
    if x in holiday:
     print('it is a holiday')
     break
else:print('it is not a holiday')
