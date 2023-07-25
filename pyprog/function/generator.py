#generator function-->these are those function
#which return a set or sequence of values; A special keyword yield is used
def generate(a,b):
    while a<=b:
        yield a
        a=a+2
k=generate(2,20)
print(k)#as this contain more valuees so it return memory location
print(list(k))
for i in k:
    print(i)

#-------------------------YIELD----------------------------------------
def janvi():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
k=janvi()
for i in k:
    print(i)
#--------------------------NEXT -----------------------------------------------   

def janvi1():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
k=janvi()
print(next(k))
print(next(k))
print(next(k))
print(next(k))













