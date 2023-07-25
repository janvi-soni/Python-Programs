from numpy import *      
a=array([int(i) for i in input("entere the elemnent to be sorted").split(',')])
for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if(a[i]<a[j]):
                a[i],a[j]=a[j],a[i]
print(a)






