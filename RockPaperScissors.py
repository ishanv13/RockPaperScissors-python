import random

# Function Creation
def game(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return False
        elif you=='s':
            return False
    elif comp=='p':
        if you=='r':
            return True
        elif you=='s':
            return True        
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True

# Taking and assigning the input
print("\nComputer's Turn: Choose Rock(r), Paper(p) or Scissor(s)")
a=random.randint(1,3)
if a==1:
    comp='r'
elif a==2:
    comp='p'
elif a==3:
    comp='s'
you=input("Your turn to Choose Rock(r), Paper(p) or Scissor(s): ")

# printing the output
if you!='r' and you!='p' and you!='s':
    print("\nInvalid Input!")
    exit()
print(f"\nComputer Choose {comp} and You Choose {you}.")
b=game(comp,you)
if b==None:
    print("\nThe Match Got Tied.")
elif b:
    print("Congrats! You Won The Match.")
else:
    print("Sorry, You Lost and computer Won.")