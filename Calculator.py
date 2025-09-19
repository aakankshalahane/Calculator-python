a =int (input("Enter first number: "))
b = int(input("Enter second number: "))
oper=input("Enter (+,-,*,/):")

if oper == '+':
 print("Addition:", a + b)
elif oper =='-':
  print("Subtraction:", a - b)
elif oper =='*':
 print("Multiplication:", a * b)
elif oper =='/':
 print("Division:", a / b if b != 0 else "Error (division by zero)")
else:
 print ("Invalid ")