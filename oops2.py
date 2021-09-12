class Calculator:
    @staticmethod
    def greet():
        print("Hello there, I am your friend calc aka calculator")
        
    def __init__(self,num) :
        self.number=num
        print("\n")

    def square(self):
        print(f"The square is, {self.number * self.number}")
        print("\n")

    def cube(self):
        print(f"The cube is, {self.number * self.number * self.number}")  
        print("\n")

    def sqroot(self):
        print(f"The square root is, {self.number ** 0.5}")          
        print("\n")

def pr():
    a=int(input("Enter a number: "))
    return Calculator(a)
    
    
a=pr()
a.square()
a.cube()
a.sqroot()
a.greet()


