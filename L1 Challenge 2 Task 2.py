import random
import string

#Functions used in the code must be defined first.
# 1: function to reverse the first name
def reverse_name(name):
  reversed_name = ''.join(reversed(name))
  return reversed_name

# 2: function to intersperse surname with first name
def intersperse_name(first_name, surname):
  empty_lst = []
  i = 0
  min_length = min(len(first_name), len(surname))
  #Use a while loop to iterate through and append the empty list
  while i < min_length:
    empty_lst.append(first_name[i])
    empty_lst.append(surname[i])
    i += 1
  #Print the remaining characters from the longer string.
  if len(first_name) > len(surname):
    while i < len(first_name):
      empty_lst.append(first_name[i])
      i += 1
  else:
    while i < len(surname):
      empty_lst.append(surname[i])
      i += 1
  #Turn list into a string
  intersperse_str = ''.join(empty_lst)
  return intersperse_str

# 3: function to split username in half and properly format the username.
def format_name(shuffled_name):
  split_point = int(len(shuffled_name)/2)
  first_half = shuffled_name[:split_point]
  second_half = shuffled_name[split_point:]
  username = first_half.title() + ' ' + second_half.title()
  return username

# 4: function to generate a random username if user selects '2'
def random_username():
  rand_name = ""
  characters = string.ascii_lowercase + string.digits
  for i in range(10):
    rand_name += random.choice(characters)
  return rand_name

#User input to pick either choice 1 or choice 2.
print("Welcome to the username creator... Please choose one of the following options: ")
print("1. Create a username based on a name")
print("2. Generate a random username")
user_choice = int(input("Enter your choice here: "))

#while loop to ensure user input is one of the 2 options specified.
while user_choice != 1 and user_choice != 2:
  user_choice = int(input("The number must be 1 or 2. Enter your choice here: "))


if user_choice == 1:
  #Ask for the user input to use as an argument in the function
  user_name = input("Please enter your name: ")
  name_backwards = reverse_name(user_name)
  #Next, ask the user for their surname.
  user_surname = input("Please enter your surname: ")
  name_shuffle = intersperse_name(name_backwards, user_surname)
  #Format the shuffled username.
  print(format_name(name_shuffle))

else:
  #Call the function to generate a random username.
  print("Your random username is: {}".format(random_username()))