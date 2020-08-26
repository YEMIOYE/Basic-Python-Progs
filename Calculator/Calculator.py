# Building a Calculator using Python

num1 = float(input('Enter first number: ')) #First Number
op = input('Enter operator: ') #Type of operator
num2 = float(input('Enter second number: ')) #Second Number

if op == '+':
    print(num1 + num2) #Sum
elif op == '-':
    print(num1 - num2) #Subtraction
elif op == '/':
        print(num1 / num2) #Division
elif op == '*':
        print(num1 * num2) #Multiplication
else:
            print('Invalid operator') #If all conditions are not met.