from random import randint

from time import sleep 

def get_user_guess():
    guess = int(input("Guess the number: "))
    return guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print("The maximum possible value is: ", max_val)
    guess = get_user_guess()
    
    if guess > max_val:
        print("Error!")
        return
    else:
        print("Rolling...")
        sleep(2)
        print("First roll :", first_roll)
        sleep(1)
        print("Second roll : ", second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print("The tatal value is : ", total_roll)
        print("Result...")
        sleep(2)
        if guess == total_roll:
            print("You have won !")
            sleep(8)
        else :
            print("You have lost !")
            sleep(8)

roll_dice(6)                    
        