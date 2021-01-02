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