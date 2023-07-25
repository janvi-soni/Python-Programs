
"""data={}
n=int(input("enter the number of items you want to enter"))
for i in range(0,n):
      k=input("enter the key")
      v=input("enter the value")
      data.update({k:v})
print(data )
print(data.keys())
for j in data.keys():
    print(j)
-------------------------------------------------
di={"janu":10,"rishu":11,"sanu":12}
name=(input("enetr the name"))
for i in di.keys():
    if name==i:
        print(di[i])


-----------------------------------------

st="golu=24,jaya=45,kumar=48"

l=[]
for i in st.split(","): 
    c=i.split("=")
    l.append(c)
print(l)
d=dict(l)
s={}
for k,j in d.items():
    s[k]=int(j)
print(s) 
------------------------------------------------------
st="1=golu,2=jaya,3=kumar"

l=[]
for i in st.split(","): 
    c=i.split("=")
    l.append(c)
print(l)
d=dict(l)
s={}
for k,j in d.items():
    k=int(k)
    s[k]=j
    
print(s)
-----------------------------------------------
d={}
for i in range(0,4):
    k=input("enter name")
    s1= input("enter subject")
    s2= input("enter subject")
    s3= input("enter subject")
    d.update({k:[s1,s2,s3]})
print(d)
sub=input("enter subject")
for i,j in d.items():
    for k in range(0,len(j)):
        if(sub==j[k]):
            print(i)
---------------------------------------------- TUPLE------------------------------------------------------------------------------          
            

t=23,4545,677,8,9,55,6,7,8,92,323,44556,7778
s=sorted(t,reverse=True)
print(s)
-----------------------------------

emp=((1001,'ajay',25000),(1002,'bhanu',20000),(1003,'jaya',3300))
print(sorted(emp,key=lambda x:x[2]))
------------------------------------------------

t=(("priya",21),("ankit",24),("mahima",2))
print(sorted(t, key=lambda x:x[0]))
t=(1,2,3,4)
t=t+(5,)
print(t)


d={}
l1=["j","k","l"]
l2=[2,3,4]
for i in range(0,len(l1)):
    k=l1[i]
    v=l2[i]
    d.update({k:v})
print(d)



d={"aa":['ab',2000,"cd"],"nepal":["sahhgd",40000,'nfdh'],"aa":["dd",20000000,"ret"]}
s=0
for i,j in d.items():
   s=s+j[1]
print(s)   """



d={1:'ananya'}
a=d.get(1)
print(a)
for i in range(0,len(a)):
    countt=0
    countt=countt+a.count(a[i])
    print(a[i] ,"occurs" ,countt,"times in",a)
    


     
































    
    
    

