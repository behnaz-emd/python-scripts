def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    if y == 0:
        print("Error !")
    return x / y

print("select operation .")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice = input("Enter 1/2/3/4 : ")

number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))

if choice == '1':
    print(f"{number1} + {number2} = {add(number1 , number2)}")
    
elif choice == '2':
    print(f"{number1} - {number2} = {subtract(number1 , number2)}")
    
elif choice == '3':
    print(f"{number1} * {number2} = {multiply(number1 , number2)}")
    
elif choice == '4':
    print(f"{number1} / {number2} = {divide(number1 , number2)}")
    
else:
    print("invalid")
