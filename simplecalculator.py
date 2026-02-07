a = int(input("Enter a first value:"))
b = int(input("Enter a second value:"))
print("select a operand:")
print("+ , add")
print("- , subtraction")
print("* , multiplication")
print("/ , division")
operator = input("Enter the operand:")
if(operator == '+'):
    print("addition:", a+b)
elif(operator == '-'):
    print("subtraction:", a-b)
elif(operator == '*'):
    print("multiplication:",a*b)
elif(operator == '/'):
    if(b>0):
        print("division:", a/b)
    else:
        print("Division by zero is not allowed")
else:
    print("invalid operator")