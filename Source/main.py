import random #import Random library

choice = random.randrange(1,10) #choice a number randomly in range 1 to 10

def guess(str):
    n = int(input(str+": ")) # get user choice 

    if n < choice:
        print("Too low")
        guess(b) # recall function

    elif n > choice:
        print("Too high")
        guess(b) # recall function

    else:
        print("Your guess it right!!")

a = "Enter your number"
b = "Enter number again"
guess(a) #call guess function
