class members:
    def __init__(self):
        self.x =100
    def disply(self):
        y=40
        print("instance variable", self.x)
        print("normal variable is", y)
n=numbers()
n.display()
print("outside the method value is: ",n.x)               
               
