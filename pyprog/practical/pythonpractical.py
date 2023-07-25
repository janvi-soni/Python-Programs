"""
for i in range(0,2):
    n=int(input("what is your favourite number"))
    if(n==0 or n==1):
        print("not prime")
    else:
        count=0

        for i in range(1,n+1):
            if(n%i==0):
                count=count+1
            
        if(count==2):
            print(n,"is prime")
        else:
            print(n,"is not prime")"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
for i in range(2000,2500):
    if(i%17==0 and i%5!=0):
        print(i)
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
a=int(input("enter the 1st no."))
b=int(input("enter the second number"))
print("before swapping:")
print(a)
print(b)
c=a
a=b
b=c
print("after swapping")
print(a)
print(b)
print("verification:")
a,b=b,a
print(a)
print(b)
"""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def largest(*n):
    c=list(n)
    d=len(c)
    for i in range(0,(d+2)):
        
        if (c[0]<c[i]):
            c[0]=c[i]
    print(c[0])

largest(2,3,4,5,6,7,8,9)
    
    
    

