# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown_list(num):
    the_list = [num]
    count = num
    while count > 0:
        count -= 1
        the_list.append(count)
    return the_list

countdown_list(5)
countdown_list(9)

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_return(num1, num2):
    print(num1)
    return num2

print_return(2,5)
print_return(7,3)

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_and_length(lst):
    first = lst[0]
    length = len(lst)
    print(first + length)
    return first + length

first_and_length([1,3,2,5,9])
first_and_length([-4,-2,5,10])

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def greater_than_2nd(lst):
    new_lst=[]
    if len(lst) == 1:
        return False
    for i in range(0, len(lst)):
        if lst[i] > lst[1]:
            new_lst.append(lst[i])
    print(len(new_lst))
    return new_lst

greater_than_2nd([5])
greater_than_2nd([9,4,3,4,8,7])

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def this_and_that(size, value):
    new_list = []
    if size < 1:
        return "Size of list is too small"
    while len(new_list) < size:
        new_list.append(value)
    return new_list

this_and_that(3,7)
this_and_that(-4,2)
this_and_that(6,1)
