## Basic concepts ##
print('Hello world')
print("Hello world")
print((2 + 2) * 4)
# an operation with / results in a float
print(3/4)
# exponentiation
print(2**5)
# square root
print(12*(1/2))
# quotient (floor division)
print(20 // 6)
# remainder
print(20 % 6)


## Strings and variables ##
print("""this prints 4 lines""")

print('naomi\'s escape \ncharacter')

print("concatenating" + "strings")
print("2" + "2")

print("This is printed 3 times" * 3)
print(3 * 'so is this')

# variables, input and type functions
integer_variable = int(input("Input an integer"))
string_variable = str(input("Input a string"))
float_variable = float(input("Input a float"))
print("These are my inputs: ", integer_variable, string_variable, float_variable)

# in-place operators
var1 = "hello"
var1 += " world"
print(var1)


## Control structures ##
# Booleans : True and False
# Boolean operators: and, or, not

# Lists
empty_list = []
my_list = [1, "two", [3]]
print("This print two: ", my_list[1])

# List operations
print("This prints a list wutg my_list appended to another my_list: ", my_list + my_list)
print("This prints a list with contents of my_list three times: ", my_list * 3)

# strings are immutable lists

# check if a value is in a list
print(1 in my_list) #prints True
print(not 1 in my_list) #prints False
print(1 not in my_list) #prints False

print(2 in my_list) #prints False
print(not 2 in my_list) #prints True
print(2 not in my_list) #prints True

# list functions
my_list.append(4)
len(my_list)
index = 0
my_list.insert(index, "zero")
print(my_list.index("zero")) # prints 0
# others: max(list), min(list), list.count(item), list.remove(item), list.reverse(), list.sort(), sorted(list, reverse=True)

# loops
for value in my_list:    
    print(value)
for value in range(10):
    print(value) # prints digits 0 to 9
while True:
    break 

# range
lower = 5
upper = 12
step = 2
print(list(range(lower, upper, step))) # [5, 7, 9, 11]
print(list(range(upper, lower, -step))) # [12, 10, 8, 6]
