""" CODE DESCRIPTION: Hangman Game."""
import random
#Define a function to generate a random word.
def random_word():
  f = open('1-1000', 'r')
  word_bank = list(f)
  computer_word = (random.choice(word_bank)).strip()
  blank_word = '_'*(len(computer_word))
  return computer_word, blank_word

#Function to edit the blank word output.
def edit_blank(user_letter, computer_word, blank_word):
  word_list = list(computer_word)
  blank_list = list(blank_word)
  for index, letter in enumerate(word_list):
    if letter == user_letter:
      blank_list[index] = letter
  blank_word = ''.join(blank_list)    
  return blank_word    

#Function to create the hangman graphic.
def hangman_graphic(guess_count):
  if guess_count == 0:
    print ("________      ")
    print ("|      |      ")
    print ("|             ")
    print ("|             ")
    print ("|             ")
    print ("|             ")
  elif guess_count == 1:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|             ")
    print ("|             ")
    print ("|             ")
  elif guess_count == 2:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /       ")
    print ("|             ")
    print ("|             ")
  elif guess_count == 3:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|      ")
    print ("|             ")
    print ("|             ")
  elif guess_count == 4:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|\     ")
    print ("|             ")
    print ("|             ")
  elif guess_count == 5:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|\     ")
    print ("|     /       ")
    print ("|             ")
  elif guess_count == 6:
    print ("________      ")
    print ("|      |      ")
    print ("|      0      ")
    print ("|     /|\     ")
    print ("|     / \     ")
    print ("|   ")

#Function to compare user guess to computer word.
def user_guess(computer_word, blank_word):
  guess_count = 0
  guess_letters = []
  hangman_graphic(guess_count)
  #While loop so that the user can guess until they get the full word.
  while blank_word != computer_word: 
    user_letter = no_repeats(guess_letters)
    guess_letters.append(user_letter)
    #See if user letter is in the word picked by the computer.
    if user_letter in computer_word:
      print("\nCorrect choice!")
      blank_word = edit_blank(user_letter, computer_word, blank_word)
    else:
      print("\nIncorrect choice!")
      guess_count += 1
      hangman_graphic(guess_count)
    blank_word = you_lost(guess_count, computer_word, blank_word, guess_letters)
  return guess_count
  
#Function to prevent user from entering repeat letters.
def no_repeats(guess_letters):
  user_letter = input('\nPlease enter a letter: ')
  while user_letter in guess_letters or len(user_letter) != 1:
    print("Please input a LETTER that you haven't guessed yet!")
    user_letter = input("\nPlease input another one: ")
  return user_letter  

#Function to check if the user has done enough guesses to lose the game.
def you_lost(guess_count, computer_word, blank_word, guess_letters):
  if guess_count >= 6:
    print("\nYou lost the game!")
    print("\nThe word was {}!".format(computer_word))
    blank_word = computer_word
    return blank_word
  elif computer_word == blank_word:
    print("\nYou won!! The word was {}.".format(computer_word))
    return blank_word
  else:
    print(blank_word)
    print("\nYou have guessed the following letters: {}".format(guess_letters))
    return blank_word

#Function to check if the user would like to play again.
def play_again():
  play_again = (input("\nWould you like to play again? (y/n) ")).lower()
  while play_again != 'y' and play_again != 'n':
    print("Enter either y or n.")
    play_again = (input("\nWould you like to play again? (y/n) ")).lower()
  return play_again
  
#Call the word generator function.
computer_word, blank_word = random_word()
print(blank_word)
while True:
  user_guess(computer_word, blank_word)
  user_choice = play_again()
  if user_choice == 'y':
    computer_word, blank_word = random_word()
    print(blank_word)
  elif user_choice == 'n':
    print("\nSee you later!")
    break
