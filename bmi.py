def calculate_bmi (hight , weight):
    bmi = weight / (hight ** 2)
    return bmi
    
hight = float (input("Enter your hight : "))
weight = float(input("Enter your weight : "))

bmi = calculate_bmi(hight , weight)
x = bmi * 10 ** 4
print(f"Your bmi is {x: .2f}")

if x < 18.5:
    print("you are underweight. ")
elif 18.5 < x < 24.9:
    print("You have a normal weight.")
elif 25 < x < 29.9:
    print("You are overweight. ")
else:
    print("You are obese. ")

