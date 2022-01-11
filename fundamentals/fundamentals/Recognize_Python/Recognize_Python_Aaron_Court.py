num1 = 42 #variable declaration, number
num2 = 2.3 #variable declaration, number
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #tuple initialize
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #dictionary, add value
print(person['name']) #log statement
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, change value
print(fruit[2]) #log statement

if num1 > 45: #if statement
    print("It's greater") #log statement
else: #else statement
    print("It's lower") #log statement

if len(string) < 5: #if statement length check
    print("It's a short word!") #log statement
elif len(string) > 15: #elseif statement, length check
    print("It's a long word!") #log statement
else: #else statement
    print("Just right!")  #log statement

for x in range(5): #for loop, start, sequence
    print(x) #log statement
for x in range(2,5): #for loop, start, stop, sequence
    print(x) #log statement
for x in range(2,10,3): #for loop, start, stop, increment
    print(x) #log statement
x = 0 #variable declaration, number
while(x < 5): #while loop, start, stop
    print(x) #log statement
    x += 1 #increment

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value at index 1

print(person) #log statement
person.pop('eye_color') #dictionary, delete value eye color
print(person) #log statement

for topping in pizza_toppings: #for loop, 
    if topping == 'Pepperoni': #if statement
        continue #for loop, continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement
        break #for loop, break

def print_hello_ten_times(): #function
    for num in range(10): #for loop
        print('Hello') #log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function, parameter
    for num in range(x): #for loop using fuction parameter
        print('Hello') #log statement

print_hello_x_times(4) #function call using arguement

def print_hello_x_or_ten_times(x = 10): #function, parameter
    for num in range(x):  #for loop using fuction parameter
        print('Hello') #log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section 
"""
#mulitline comment

# print(num3) - NameError: name num3 is not defined
# num3 = 72 
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'