def switch_case(case):
    if case==1:
        print("Brocode-1")
    elif case==2:
        print("Brocode-2")
    elif case==3:
        print("Brocode-3")
    else:
        print("Invalid Choice")
switch_case(1)
switch_case(2)
switch_case(3)
switch_case(4)

#dic mapping using switch case
def switch_case(case,num1,num2):
    switcher={
        "Add":num1+num2,
        "Subtract":num1-num2,
        "Multiply":num1*num2,
        "Divide":num1/num2
    }
    result=switcher.get(case,"Invalid")
    print(result)

switch_case("Add",10,5)
switch_case("Subtract",10,5)
switch_case("Multiply",10,5)
switch_case("Divide",10,5)

def calculate(operation, num1, num2):
    switcher = {
        "add": lambda: num1 + num2,
        "subtract": lambda: num1 - num2,
        "multiply": lambda: num1 * num2,
        "divide": lambda: num1 / num2
    }
    result = switcher.get(operation, lambda: "Invalid operation")
    return result()

print(calculate("add", 10, 5))
print(calculate("subtract", 10, 5))
print(calculate("multiply", 10, 5))
print(calculate("divide", 10, 5))
print(calculate("power", 10, 5))

#Using lambda function
def calculate(operation, num1, num2):
    switcher = {
        "add": lambda: num1 + num2,
        "subtract": lambda: num1 - num2,
        "multiply": lambda: num1 * num2,
        "divide": lambda: num1 / num2
    }
    result = switcher.get(operation, lambda: "Invalid operation")
    return result()

print(calculate("add", 10, 5))
print(calculate("subtract", 10, 5))
print(calculate("multiply", 10, 5))
print(calculate("divide", 10, 5))
print(calculate("power", 10, 5))