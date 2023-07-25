#function decorators-a decorator function is a function that accepts another function as a parameter modifies it and returns a functions

def decor(f):
    def inner():
        val=f()
        return val+2
    return inner
def fun():
    return 10
k=decor(fun)#decorator function
print(k())
print("-----------------------------------------------------------")
#-------------------------------------------------------------------------------------------------------------------------------
def decor0(f):
    def inner():
        val=f()
        return val+2
    return inner
@decor0
def fun():
    return 10
#decorator function
print(fun())
print("-----------------------------------------------------------")

#------------------------------------------------------------------------------------------------------------------------------------
def decor1(ff):
    def inner():
        val=ff()
        return val+10
    return inner
def decor2(ff):
    def inner():
        val=ff()
        return val*2
    return inner
   
def num():
    return 10
res=(decor1(decor2(num)))
print(res())
    
#------------------------------------------------------------------------------------------------------------------
def decor11(fff):
    def inner():
        val=fff()
        return val+10
    return inner
def decor22(fff):
    def inner():
        val=fff()
        return val*2
    return inner
@decor11
@decor22
def num1():
    return 10
print(num1())
    
