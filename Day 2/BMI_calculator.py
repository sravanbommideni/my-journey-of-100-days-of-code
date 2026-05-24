import sys
print("""welcome to Body Mass Index calculator!""")

unit_weight = input("""In which SI unit you have your weight?(kg or pound) : """)
if unit_weight in ["kg","kgs","kilograms"] :
    weight=float(input("""enter your weight : """))
elif unit_weight in ["pound","lbs","pounds"] :
    lbs=float(input("""enter your weight :"""))
    weight=lbs*0.45
else :
    print("""invalid unit of weight!!""")
    weight = None
    sys.exit()

unit_height = input("""in which SI unit you have your height?(centimeter or feet) :""")
if unit_height in ["cm","centimeters"] :
    height_1=float(input("""enter your height : """))
    height= (height_1)/100
elif unit_height in ["feet","ft"] :
    ft=float(input("""enter your height :"""))
    height=ft/(3.28)
else :
    print("""invalid unit of height!!""")
    height = None
    sys.exit()

BMI = weight/(height**2)
if weight is not None :
    if height is not None :
        print(f"""your BMI is :{BMI:.2f}""")