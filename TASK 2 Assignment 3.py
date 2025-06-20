#This program will not run for "number <= 0"
#Improting the math module
import math

#For asking the input from the user
number = float(input("Enter a number: "))

#For calculations
def calculations(a):
    print(f'Square root: {math.sqrt(a)}')
    print(f'Logarithm: {math.log(a)}')
    print(f'Sine: {math.sin(a)}')

#Calling the function
calculations(number)
