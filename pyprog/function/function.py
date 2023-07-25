
"""--------------------------------------------------------------------ADD----------------------------------------------------------------------------------------------------
def add(a,b):
    return a+b;
c=add(12,5)
print(c)
-------------------------------------WE CAN RETURN MULTIPLE VALUES IN PYTHON UNLIKE OTHER LANGUEGES WHICH RETURNS ONLY 1----------------------------------------------
def calc(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f
j=int(input("enter the number"))
k=int(input("enter the number"))
w,x,y,z=calc(j,k)
print("add : ",w);
print("sub : ",x);
print("mul : ",y);
print("div : ",z);
---------------------------------------------------------calculator(RETURN VALUES IN TUPLE)---------------------------------------------------------------------------------------------------
def calc(a,b):
    return a+b,a-b,a*b,a/b
j=int(input("enter the number"))
k=int(input("enter the number"))
print(calc(j,k))
----------------------------------------------------------WE CAN CALL A FUNCTION INSIDE ANOTHER FUNCTION ----------------------------------------------
def janvi(s):
    def message():
        return "how are you!"
    r=message()+s
    return r
k=input("enter the name")
print(janvi(k))
--------------------------------------------------------------------------------------
def findelement(lis,a):
    for i in range(0,len(lis)):
        if a in lis:
            print("found at index", i)
    else:
         print("not found")
list=[1,2,3,4,5,6,7,8]
n=int(input("enter the element")
findelement(list,n)      
----------------------------------- finding avg of population---------------------------------------------------------------------------------
def findavg(dict):
    s=0
    for i in d.values():
        s=s+i[1]
        b=s/len(dict)
    print(b)
d={'a':['a1',5000,'a2'],'b':['b1',56000,'b2'],'c':['c1',90000,'c2'],'d':['d1',30000,'d2'],'e':['e1',80000,'e2']}
findavg(d)
#-------------------------------------------------CHECKPALINDROME-------------------------------------------------------------
def chkpalindrome(j):
    a=j
    rev=0
    while(j>0):
        b=j%10
        rev=rev*10 + b
        j=j//10
    if(a==rev):
        return True;
    else:
        return False;

n=int(input("enetr the number up to u want palindrome no."))
for i in range(1,n):
      if chkpalindrome(i):
          print(i)
#------------------------------------------------------ CHECK PRIME OR NON PRIME NUMBER---------------------------------------------------------------
def chkprime(n):
    count=0
    if(n==0 or n==1):
        print("non prime")
    for j in range(1,n+1):
        if(n%j==0):
            count=count+1
    if(count==2):
        print(n ,"is prime")
    else:
        print(n,"is non prime")                #2 IS PRIME 3 IS PRIME 4 IS NON PRIME
    
for i in range(0,100):
    chkprime(i)
     
#--------------------------------------------------PRINT PRIME NUMBERS-------------------------------------------------------------
def chkprime(n):
    count=0
    for j in range(1,n+1):
        if(n%j==0):
            count=count+1
    if(count==2):
        return True
                 
print("prime are:")   
for i in range(0,100):
    if chkprime(i):
        print(i)

                 #2357111317
    
#-------------------------------------------------------CHECK PERFECT NUMBER------------------------------------------------------------
def chkperfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if sum==n:
        print(n,"is perfect")
    else:
        print(n,"is not a perfect number")
for i in range(0,100):
    chkperfect(i)
    """
def fun():
    def message():
        return("have fun")
    def display(fun):
        return "rahul"+fun
fun()












      

      
      
    


