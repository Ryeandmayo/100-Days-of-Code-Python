#calculator
from art import logo
#add
def add (n1, n2):
  return n1 + n2

#subtract
def subtract (n1, n2):
  return n1 - n2

#multiply
def multiply (n1, n2):
  return n1 * n2  

#divide
def divide (n1, n2):
  return n1 / n2

operations = {"+": add,
   "-": subtract,
  "*": multiply,
  "/": divide,
  }
def calculator():
  print(logo)
  
  num1 = float(input("whats the first number?  "))
  num2 = float(input("whats the second number?  "))
  
  for symbol in operations:
    print(symbol)
    
  operation_symbol = input("Pick an operation from the line above: ")
  answer = operations[operation_symbol](num1, num2)  
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  is_finished = False
  
  while not is_finished:
    continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:  ")
    if continue_calculation == "y":
      operation_symbol = input("Pick an operation: ")
      num3 = float(input("whats the next number?  "))
      answer = operations[operation_symbol](answer, num3)
      print(f"{answer} {operation_symbol} {num3} = {answer}")
    else:
      is_finished = True
      calculator()
calculator()