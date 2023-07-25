
f=open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'w')
st=input("enter something")
f.write(st)
f.close()
# if we run it again and write something it will overwrite the previous content in that particular file
#---------------------------------------------------------------------------
f1=open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'r')
d=f1.read()
f1.close()
print(d)
#-------------------------------------------------------------------------------
with open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'w')as f:
    s=input("enter something")
    f.write(s)
# if we open a file by using with you no need to close a file

#----------------------------------------------------------------------------
f2=open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'a')
str=input("enter something to append")
f2.write(str)
f2.close()
# 'a' mode append the data to the previous file
#----------------------------GOING THROUGH THE FILE-------------------------------------------------
f=open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'w')
print("enter something")
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+'\n')
f.close()
#------------------------------------------------------------------------------------------
import os,sys
s=input("enter the file name with extension")
if os.path.isfile(s):
    f=open(s,"w")
    ch=input("enter something to write in a file")
    f.write(ch)
    f.close()
else:
    print("file not exist")
    sys.exit()
#-------------------------------------------------------------------------------------------

f=open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'r')
d=f.read()
f.close()
count=0
for b in d:
    
    if (b==a or b==e or b==i or b==o or b==u):
        count=count+1
print(count)
            



























    

   
