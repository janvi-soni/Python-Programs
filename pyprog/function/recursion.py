"""------------------------------------------------------------------RECURSION FACTORIAL---------------------------------------------------------------------------------
def fact(n):
    if(n==0):
        res=1
    else:
        res=n*fact(n-1)
    return res    

for i in range(1,30):
    print("factorial of ",i ,"is :",fact(i))
-------------------------------------------------------------------WAP TO SORT A LIST USING BINARY SEARCH ALGORITHM AND RECURSION----------------------------------------------    
"""
"""
def binary(listt,start,stop,sv):
    if start>stop:
        return -1
    mid=(start+stop)//2
    if(sv>listt[mid]):
        return binary(listt,mid+1,stop,sv)
    elif sv>listt[mid]:
        return binary(listt ,start,mid,sv)
    else:
        return mid
n=[2,48,5,78,6,85,59,4,4,445,60,67,8,98,89,9,889,22,3,3,44,55,66,7,998]
n.sort()
print(n)
srch=int(input("enter the no. to search"))
ind=binary(n,0,len(n),srch)
if(ind<0):
    print("value not found")
else:
    print("value found at",ind)
v"""

