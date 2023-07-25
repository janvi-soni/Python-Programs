from data import emp
import pickle
f=open(r"C:\Users\janvi soni\Desktop\rishabh.dat",'wb')
#wb stands for write binary and dat extension contain data in binary format
n=int(input("enter the no of emplyoees"))
for i in range(0,n):
    n=input("enter the name")
    a=int(input("enter the age"))
    s=int(input("enter the sal"))
    e=emp(n,a,s)
    pickle.dump(e,f)
f.close()
#_-------------------------------------------------------------------------
from data import emp
import pickle
f=open(r"C:\Users\janvi soni\Desktop\rishabh.dat",'rb')#readbinary
while True:
    try:
        j=pickle.load(f)
        j.display()
    except EOFError:
        print("no more data found")
        break
f.close()
