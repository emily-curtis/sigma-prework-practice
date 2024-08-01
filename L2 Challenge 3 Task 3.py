def num_obj(s):
  empty_lst = []
  #Loop through each number in the input argument
  for number in s:
    letter = chr(number)
    empty_lst.append({str(number):str(letter)})
  return empty_lst

print(num_obj([118, 117, 120]))
