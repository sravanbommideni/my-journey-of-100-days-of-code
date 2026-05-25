import random,sys
print("Welcome to the Game!!!")
print("What do u choose?Type 0 for Rock , Type 1 for Paper and Type 2 for Scissors")
user=int(input())
if user==0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif user==1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif user==2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
else :
    print("enter valid input!!!")
    sys.exit()
computer=["rock" , "paper" , "scissor"]
print("computer choose:")
us=random.choice(computer)
if us=="rock":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif us=="paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif us=="scissor":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if user==0 :
    if us=="scissor":
        print("You won")
    elif us=="rock":
        print("tie")
    else :
        print("you lost")
elif user==1 :
    if us=="rock":
        print("You won")
    elif us=="paper":
        print("tie")
    else:
        print("you lost")
elif user==2 :
    if us=="paper":
        print("You won")
    elif us=="scissor":
        print("tie")
    else :
        print("you lost")
