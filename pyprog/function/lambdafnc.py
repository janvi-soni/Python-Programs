##f=lambda x:x*x
#print(f(5))
#--------------------------------------------------------------------------------------------------------------------------------------------------
#f=lambda x,y:x+y
#print(f(6,30))
#-----------------------------------------------------------------------------------------------------------------------------------------------
#f=lambda x,y:x if(x>y) else y
#print(f(34,55))
#--------------------------------------------------------------------FILTER FUNCTION-------------------------------------------------------------
#filter(func,collection))
n=[21,34,43,41,25,25,21,55,52,40,54,64,88,21]
def evennum(x):
    if x%2==0:
        return True;
    else:
        return False;
print(list(filter(evennum,n)))
#clone by lambda
n=[21,34,43,41,25,25,21,55,52,40,54,64,88,21]
def evennum(x):
    if x%2==0:
        return True;
    else:
        return False;
print(list(filter(evennum,n)))











