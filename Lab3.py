#Stephen Larsen, 1407008
#Lec B1
#Lab H02
#Program asks user to guess a number 1-100
#Continues until guess is correct, informs user if guess is too high or low
#Counts number of times guessed

#Assign value
import random
number = random.randint(1,100)

#Initial input
count = 1
guess = int(input("Guess a number between 1 - 100: "))

#Checks
while guess>number or guess<number:
    if guess>number:
        print("You guessed too high")
        guess = int(input("Guess a number between 1 - 100: "))
        count = count+1

    else:
        print("You guessed too low")
        guess = int(input("Guess a number between 1 - 100: "))
        count = count+1

print("Correct! The number was",number,"and you guessed",count,"times.")