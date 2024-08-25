def farenheit_celsius(farenheit):
    return (farenheit * 5/9) - 32


def celsius_farenheit(celsius):
    return (celsius * 9/5) + 32

print("Temperature Conversion \n Enter your choice : ")
print("1. farenheit to celsius. ")
print("2. celsius to farenheit. ")

choice = input("Enter your choice : ")

if choice == '1':
    farenheit = float(input("Enter temperture : "))
    print(f"{farenheit}f is {farenheit_celsius(farenheit)}c")
    
elif choice == '2':
    celsius = float(input("Enter temperture : "))
    print(f"{celsius}c is {celsius_farenheit(celsius)}f")
    