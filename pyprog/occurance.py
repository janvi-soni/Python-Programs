d={1:'ananya'}
a=d.get(1)
a=list(a)
a.sort()
print(a)
for i in range(0,len(a)):
    countt=0
    countt=countt+a.count(a[i])
    if(a[i-1]!= a[i]):
        print(a[i] ,"occurs" ,countt,"times ")
    
