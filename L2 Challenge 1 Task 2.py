#Given a random  non-negative number, return the digits of this number within an array in 
#reverse order.
def digitize(n):
    #Convert the int to a string and then the str to a list
    n_list = list(str(n))
    new_numbers = []
    for n in n_list:
        new_numbers.append(int(n))
    reverse_lst = new_numbers[::-1]

    return reverse_lst
        

num1 = 123
print(digitize(num1))        