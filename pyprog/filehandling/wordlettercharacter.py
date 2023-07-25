#TOTAL NO OF WORDS LINE AND LETTERS IN A FILE
f=open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'r')
w=0
cw=cc=cl=0
for i in f:
    cl=cl+1
    w=i.split()
    cw=cw+len(w)
    cc=cc+len(i)
print("lines",cl)
print("words",cw)
print("character",cc)


