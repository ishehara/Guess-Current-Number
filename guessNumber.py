import random
def guess_number():
    hiddenNumber=random.randint(1, 10) # it guessing numbers between 1 to 10, including 1 and 10
    yourInput=0
    while yourInput!=hiddenNumber:
        yourInput=int(input("Input a number: "))
        if yourInput>hiddenNumber:
            print("Too high, Try again...")
        elif yourInput<hiddenNumber:
            print("Too low, Try again...")
        else:
            print("You won...")


guess_number()