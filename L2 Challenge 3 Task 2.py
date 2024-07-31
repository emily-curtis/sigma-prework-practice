#Function to deal with the scenario where the user enters nothing.
def nothing_entered(user_input):
  while user_input == '':
    user_input = input('Please enter a valid input. ')
  return user_input
#Function to print out the details of the list.
def user_details(people):
  for person in people:
    print("Name: {} {} \n Age: {}\n Employed: {}\n".format(person['first_name'], person['last_name'], person['age'], person['employment']))
#Function to ask user whether they would like to add or remove a dictionary item.
def add_or_remove():
  user_input = (input("Would you like to 'Add' or 'Remove' from the array? Please enter your answer: ")).lower().title()
  while user_input != 'Add' and user_input != 'Remove':
    user_input = input("You must enter either 'Add' or 'Remove. Please enter your answer: ")
    user_input = user_input.lower().title()
  return user_input  
#Function to add a dictionary entry.
def add_entry(people):
  name1 = (input("Please enter your first name: ")).lower().title()
  name2 = (input("Please enter your second name: ")).lower().title()
  new_age = input("Please enter your age: ")
  employed = (input("Please enter 'Yes' or 'No' regarding employment status: ")).lower().title()
  people.append({'first_name': name1, 'last_name': name2 , 'age': new_age , 'employment': employed})
  return people
#Function to remove a dictionary entry.
def remove_entry(people):
  which_user = (input("Which user would you like to remove from 'people'? ")).lower().title()
  for person in people:
    if which_user == person['first_name']:
      people.remove(person)
  return people    

  
person_1 = {'first_name': 'Jane', 'last_name': 'Doe', 'age': 42, 'employment': 'Yes'}
person_2 = {'first_name': 'Tom', 'last_name': 'Smith', 'age': 18, 'employment': 'Yes'}
person_3 = {'first_name': 'Mariam', 'last_name': 'Coulter', 'age': 66, 'employment': 'No'}
person_4 = {'first_name': 'Gregory', 'last_name': 'Tims', 'age': 8, 'employment': 'No'}
people = [person_1, person_2, person_3, person_4]
#Iterate over array and print each person's details to the console.
user_details(people)
#Ask user whether to 'Add' or 'Remove'. Input will only accept these 2 answers.
user_input = add_or_remove()
#Define while loop to show the input prompt again after the code has run.
while user_input == 'Add' or user_input == 'Remove':
  #If user types 'Add' show inputs in the console that will ask for the user's name, age and if they are employed or not. 
  if user_input == 'Add':
    add_entry(people)
  elif user_input == 'Remove':
    remove_entry(people)                  
  user_details(people)
  user_input = add_or_remove()