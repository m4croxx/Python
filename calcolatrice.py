import math 

print ('''
    WELCOME TO THE CALCULATOR!
     what do you want to do?''')
calculation = input ('''
      Addition --------> +
      Subtraction -----> -
      Multiplication --> x
      Division --------> /
      Power------------> ^
      Square Root------> cube
        
                ''')
calculation = calculation.lower()
while not (calculation == '+' or calculation == '-' or calculation == 'x' or calculation == '/' or calculation == '^' or calculation == 'cube'):
  print("please user, choose a type of operation")
  calculation = input ('''
      Addition --------> +
      Subtraction -----> -
      Multiplication --> x
      Division --------> /
      Power------------> ^
      Square Root------> cube
        
                ''')

if (calculation == '+' or calculation == '-' or calculation == 'x' or calculation == '/'):
  num1 = int (input ('''what is the first number?'''))
  num2 = int (input ('''what's the second number?'''))
if (calculation == '^'):
  num1 = int (input ('''what is the base?'''))
  num2 = int (input ('''what's the exponent?'''))
if (calculation == 'cube'):
  num = int (input ('''at what number do you want to calculate the square root?'''))

if calculation  == "+":
  print("you have selected addition")
  sum = (num1 + num2)

if calculation  == "-":
  print("you have selected subtraction")
  sum = (num1 - num2)

if calculation  == "x":
  print("you have selected multiplication")
  sum = (num1 * num2)

if calculation  == "/":
  print("you have selected the division")
  sum = (num1 / num2)

if calculation  == "^":
  print("you have selected the power")
  sum = (num1 ^ num2)

if calculation  == "cube":
  print("you have selected the square root")
  sum = (math.sqrt(num)) 

print("the result is...", sum)