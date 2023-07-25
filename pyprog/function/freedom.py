class student:
    def __init__(self,n,a):                     #this is just like constructor in java
        self.name=n
        self.age=a
    def talk(self):
        print("hello",self.name)
        print("your age",self.age)
