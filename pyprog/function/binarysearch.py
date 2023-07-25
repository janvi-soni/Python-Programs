"""
---------------------------------------------------------------BINARY SEARCH--------------------------------------------------------------------------
n=[42,55,21,11,88,5,4,122,1,115]
n.sort()
mid=len(n)//2
c=False
sv=int(input("enter the element to search"))
if sv==n[mid]:
    print("found at ",mid)
    c=True
elif sv>n[mid]:
    for i in range(mid+1,len(n)):
        if n[i]==sv:
           print("found at ",i)
           c=True
elif sv<n[mid]:
    for i in range(0,mid):
        if sv==n[i]:
            print("found at ",i)
            c=True
elif c==False:
    print("not found")
--------------------------------------------------------------------REVERSE BINARY SEARCH ---------------------------------------------------------------------
n=[42,55,21,11,88,5,4,122,1,115]
n.sort(reverse=True)
print(n)
mid=len(n)//2
c=False
sv=int(input("enter the element to search"))
if sv==n[mid]:
    print("found at ",mid)
    c=True
elif sv<n[mid]:
    for i in range(mid+1,len(n)):
        if n[i]==sv:
           print("found at ",i)
           c=True
elif sv>n[mid]:
    for i in range(0,mid):
        if sv==n[i]:
            print("found at ",i)
            c=True
elif c==False:
    print("not found")
