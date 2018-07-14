for i in range (1,1000):
    t=i
    s=0
    while(i!=0):
        rem=i%10
        s=s+(rem**3)
        i=i//10
    if(s==t):
        print(s)
        
