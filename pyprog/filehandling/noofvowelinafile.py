f=open(r"C:\Users\janvi soni\Desktop\janvifile.txt",'r')
d=f.read()
f.close()
count=0
for b in d:
    if (b=='a' or b=='e' or b=='i' or b=='o' or b=='u'):
        count=count+1
print(count)
            


