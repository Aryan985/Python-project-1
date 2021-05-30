import random
print ("Number Guessing Game")
number = random.randint(1,9)
chance = 0
print ("Guess a Number (Between 1 to 9) ")
while chance <5:
    guess = int(input("Enter your guess:- "))


    if guess == number:
        print("Congratulation YOU WON!!!")
        break


    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)


    else:
        print("Your guess was too high: Guess a number lower than", guess)

   
    chance += 1


if not chance < 5:
    print("YOU LOSE!!! The number is", number)