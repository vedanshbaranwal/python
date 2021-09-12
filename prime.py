a=int(input("enter a number"))
prime=True
for item in range(2,a):
   if (a%item==0):
       prime=False
       break
if prime:
    print("prime")
else:
    prime("not prime")    
