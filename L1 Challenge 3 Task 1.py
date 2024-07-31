#Function to check if user input is an integer
def ask_user_for_number():
  while True:
    user_number = input("Please enter a number: ")
    try:
      int(user_number)
      break
    except ValueError:
      print("This is not an integer number.")
  return int(user_number)

#Function to ask user for sum or product
def ask_user_for_sum():
  sum_prod = input("Would you like to calculate the 'sum' or 'product'? ")
  while sum_prod != 'sum' and sum_prod != 'product':
    print("Invalid input. Please enter either 'sum' or 'product'.")
    sum_prod = input("Would you like to calculate the 'sum' or 'product'? ")
  return sum_prod
#Function to calculate sum from 1 to n
def number_sum(num1):
  sum = 0
  for num in range(num1+1):
    sum += num
  return sum

#Function to calculate product from 1 to n
def number_product(num1):
  sum = 1
  for num in range(1,(num1+1)):
    sum *= num
  return sum

#Function to calculate sum only if multiple of 3 or 5
def multiples_three_five(num1):
  sum = 0
  for num in range(num1+1):
    if num % 3 == 0 or num % 5 == 0:
      sum += num
  return sum

#Function to calculate either the sum or the product
def sum_or_product(num1):
  sum_prod = ask_user_for_sum()
  if sum_prod == 'sum':
    result = number_sum(num1)
  elif sum_prod == 'product':
    result = number_product(num1)
  return result

#Area to call functions.
user_num = ask_user_for_number()
print(number_sum(user_num))
print(multiples_three_five(user_num))
print(sum_or_product(user_num))