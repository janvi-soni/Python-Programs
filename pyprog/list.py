a=[2,3,4,5]
a.append(6)#append
print(a)

a=[22,3,4,5]
a.sort()#sort
print(a)
a.reverse()#reverse
print(a)


c=[5,7,89,898,9]
b=[7,8,9]
c.extend(b)#extend
print(c)

lis=[4,5,5,1,2,5,5]#index
print(lis.index(5)) #1


lis=[4,5,5,1,2,5,5]
lis.clear()#clear
print(lis)#[]

lis=[4,5,5,1,2,5,5]
a=lis.count(5)
print(a)#4

lis=[4,5,5,1,2,5,5]
a=lis.copy()
print(a)

lis=[4,5,5,1,2,5,5]
lis.insert(4,12)#(index,value)#[4,5,5,1,12,2,5,5]
print(lis)

lis=[4,5,5,1,2,5,5]
lis.pop()
print(lis)

lis=[4,5,5,1,2,5,4]
lis.remove(4)
print(lis)

