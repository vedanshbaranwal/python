def convert(num):
    return (num/30.48)

a=int(input("Enter the height in Centi Meter to convert in feet : "))
a=convert(a)
print(a)