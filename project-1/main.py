import random

def gameWin(comp , you):
    if(comp == you):
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False
    

randNo = random.randint(1,3)
if(randNo==1):
    comp="s"
elif(randNo==2):
    comp="w"
elif(randNo==3):
    comp="g"
print("comp turn : " )
you = input("Your turn snake(s) water(w) gun(g) : ")
c = gameWin(comp , you)

if(c):
    print("You win")
elif(c == False):
    print("You loss")
else:
    print("The match tie")