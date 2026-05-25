height=int(input("enter your height:"))
weight=float(input("enter your weight:"))

BMI = weight/(height**2)
print(f"your BMI is {BMI} and\n")
if BMI>=25 :
    print("you are overweight! , you need to hit the gym...")
elif BMI>=18.5 :
    print("you are good! , maintain it like that.")
else :
    print("you are underweight! , you need to eat...")