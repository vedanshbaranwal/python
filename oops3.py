class school:
    def __init__(veda, name, classes, admissioncharge):
        veda.name = name
        veda.classes = classes
        veda.admissioncharge = admissioncharge

    def getstatus(veda):
        print(
            f"The school is {veda.name}, the number of classes are {veda.classes}")

    def getprice(veda):
        print(f"The admission charge for school is {veda.admissioncharge}")


AVM = school("AVM", 12, 10000)
GEMS = school("GEMS", 12, 13000)
DAV = school("DAV", 12, 11000)
RATOBANGLA = school("RATOBANGLA", 12, 15000)
LA = school("LA", 12, 20000)

print ("LIST FOR SCHOOLS:")

print ("AVM", "GEMS", "DAV", "RATOBANGLA", "LA", "\n" )

print("What do you want to check Status or Admission charge of which school? \n For Status type s and for Admissioncharge type a \n")

b = "s"
c = "a"
avm = "AVM"
gems = "GEMS"
dav = "DAV"
ratobangla = "RATOBANGLA"
la = "LA"

a = input("Enter your choice: ")
v = input("Enter name for school: ")

if(b in a and avm in v):
    AVM.getstatus()

if(b in a and gems in v):
    GEMS.getstatus()

if(b in a and dav in v):
    DAV.getstatus()

if(b in a and ratobangla in v):
    RATOBANGLA.getstatus()

if(b in a and la in v):
    LA.getstatus()

if(c in a and avm in v):
    AVM.getprice()

if(c in a and gems in v):
    GEMS.getprice()

if(c in a and dav in v):
    DAV.getprice()

if(c in a and ratobangla in v):
    RATOBANGLA.getprice()

if(c in a and la in v):
    LA.getprice()



