import random
comp=random.randint(1,3)
if comp == 1:
    comp= "rock"

if comp == 2:
    comp= "paper"

if comp == 3:
    comp= "scissor"      

# def game(you,comp):
#     if you==comp:
#         return None

#     elif you=="rock":
#         if comp=="paper":
#             return False


#     elif you=="paper":
#         if comp=="scissor":
#             return False            

#     elif you=="scissor":
#         if comp=="paper":
#             return False
            
#     elif you=="rock":
#         if comp=="scissor":
#             return True
            
#     elif you=="paper":
#         if comp=="rock":
#             return True
            
#     elif you=="scissor":
#         if comp=="paper":
#             return True

def game(comp, you):
    if comp==you:
        return None

    elif comp=="rock":
        if you=="scissor":
            return False
        elif you=="paper":
            return True

    elif comp=="scissor":
        if you=="paper":
            return False
        elif you=="rock":
            return True 

    elif comp=="paper":
        if you=="rock":
            return False
        elif you=="scissor":
            return True         

        
                        
you=input("Enter your move: \n 1.Rock 2.Paper 3.Scissor \n")          
a=game(comp, you)
print()
print(f"Computer chose {comp}")
print(f"You chose {you}\n")

if a==None:
    print("Its a tie")
elif a==False:
    print("You lose and computer win")    
else:
    print("You win")
v=input()