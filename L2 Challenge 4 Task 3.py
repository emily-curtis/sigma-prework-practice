def say_hello_to_pets(pets):
  for pet in pets:
    hello_message = ""
    if pet["type"] == "dog":
      hello_message = "Woof"
      pet_name = pet['name']
    elif pet["type"] == 'cat':
      hello_message = "Meow"
      pet_name = pet['name']
    elif pet["type"] != ('cat' or 'dog'):
      raise Exception("Only cats and dogs allowed!")
    
    print(f"{hello_message}, {pet_name}!")

animals = [{'name': 'Fluffy', 'type': 'dog'},
  {'name': 'Parsley', 'type': 'dog'},
  {'name': 'Ginger', 'type': 'cat'},
  {'name': 'Biscuit', 'type': 'cat'},
  {'name': 'Poppet', 'type': 'cow'} ]

if __name__ == "__main__":
  say_hello_to_pets(animals)