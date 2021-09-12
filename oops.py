

class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name  
        self.product=product

    def intro(self):
        print(f"The name is {self.name}, the product is {self.product}")     

def search():
    a=input("Enter name: ")
    b=input("Enter product: ")
    return Programmer(a,b)
    

employee=search()
employee.intro()    
