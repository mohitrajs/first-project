import random
a=str(input("enter the input"))
print("user_choice=",a)
b=["rock","scissor","paper"]
c=random.choice(b)
print("computer choice=",c)
if a=="rock":
    if c=="rock":
        print("draw")
    elif c=="paper":
        print("computer is winner")
    else:
        print("computer is winner")
elif a=="paper":
    if c == "rock":
        print("user is winner")
    elif c == "paper":
        print("draw")
    else:
        print("computer is winner")
elif a=="scissor":
    if c == "rock":
        print("computer is winner")
    elif c == "paper":
        print("user is winner")
    else:
        print("draw")
        

