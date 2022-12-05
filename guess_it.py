import random
randno=random.randint(1,100)
#3print(randno)
userguess=None
guess=0
while(userguess!=randno):
    userguess=int(input("enter your guess "))
    guess+=1
    if(userguess==randno):
        print("you guessed it right")
    else:
        if(userguess<randno):
            print("you guessed it wrong guess a larger no")
        else:
            print("you guessed it wrong guess a smaller no")
print(f"you have taken {guess} guess to give right answer")
with open("highscore.txt","r") as f:
    content=int(f.read())
if (guess<content):
    print("new highscore")
    with open("highscore.txt", "w") as f:
            f.write (str(guess))
