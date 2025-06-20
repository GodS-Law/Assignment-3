#This is made using loop
#This is for taking value from the user
value = int(input('Enter a number: '))

#Calculating the factorial
val = 1
def trial(g):
    global val
    for i in range(1,g + 1):
        val = val * i
    print(f'Factorial of {value} is: {val}')

#Executing function
trial(value)

'''
#This is made using recursion
#This is for calculating factorial
def factorial(a):
    if a < 2:
        return 1
    else:
        return a * (factorial(a-1))

#To assign the calculated value to the variable "result"
result = factorial(value)

#To print the result
print(f'Factorial of {value} is: {result}')
'''