def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
        print("ERROR!")
    return x / y

def greet_user():
    name=input("Whats your name: ").strip().title()
    return name

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operations = input("Choose (+,-,*,/):"  ).strip()

    if operations == "+" :
        return add (num1 , num2)
    elif operations == "-":
        return subtract(num1, num2)
    elif operations == "*":
        return multiply(num1,num2)
    elif operations == "/":
        return division(num1,num2)
    else:
        return "ERROR! invalid input"



print(f"Hello {greet_user()}")
result=calculator()
print(f"TOTAL: {result}")
