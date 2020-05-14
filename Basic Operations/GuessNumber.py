import random

takenNumber=random.randint(0,200)
live=3
print("\n\n#####\tWelcome to the game!\t#####\nGuess a number which is taken by computer.\n Between 0 to 200 and you have 3 live for guess.")
while live > 0:
    usr_input = int(input("What is your number: "))
    if usr_input == takenNumber:
        print("Cong! You have "+live+" live point.")
        break;
    elif usr_input>takenNumber:
        live-=1
        print("The number is lower than your guess.\nYour live point is ",live)
    elif usr_input<takenNumber:
        live-=1
        print("The number is higher than your guess.\nYour live point is ",live)
if live==0:
    print("The number is: "+ str(takenNumber) +"\nMaybe next time..")
