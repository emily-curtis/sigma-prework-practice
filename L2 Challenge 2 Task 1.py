#Code a guessing game where the user guesses a secret number.
#After every guess the program tells the user whether their number was too large or too small.
#Keep count of how many tries the user has attempted.
#At the end of the game the number of tries should be printed.
#It should only count as one try if they input the same number multiple times consecutively.
#When the user inputs the correct number the program should show a 'You Won!' message. 
import random
#Function to determine if user input is high or low
def high_or_low(user_num, secret_num):
    #If loop to check if number is higher or lower.
        if user_num > secret_num:
            print("Your guess was too high!")
        elif user_num < secret_num:
            print("Your guess was too low!")

#Function to generate a secret number and compare it to the user input.
def secret_number():
    secret_num = random.randint(1, 100)
    user_num = 0
    tries_count = 0
    previous_guess = 0
    #While loop is needed to keep track of whether the user has guessed correctly.
    while user_num != secret_num:
        user_num = int(input("Please enter a guess: "))
        if tries_count > 0 and previous_guess == user_num:
            print("You guessed the same number.")
            continue
        previous_guess = user_num
        high_or_low(user_num, secret_num)
        tries_count += 1  
    print("You won! The secret number was {}!".format(secret_num))
    return "Number of tries: {}".format(tries_count)            

print(secret_number())
