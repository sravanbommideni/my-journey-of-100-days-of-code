def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def divide(num1,num2):
    return num1/num2
def multiply(num1,num2):
    return num1*num2

operators={
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
}
def calculator():
    """hiiii"""
    continue_calculating=True
    first_operand=float(input("enter first operand :"))

    while continue_calculating:
        for key in operators:
            print(key)
        operator=input("enter an operator :\n")
        while operator not in operators:
            operator = input("enter a valid operator :\n")
        second_operand=float(input("enter second operand :"))
        result=operators[operator](first_operand,second_operand)
        print(f"{first_operand}{operator}{second_operand}={result}")
        continue_caluclation=input(f"type yes to continue calculating with {result}? type no for starting a new calculation :\n")

        if continue_caluclation=="yes":
            first_operand=result
        else:
            continue_calculating=False
            print("\n"*50)
            calculator()

calculator()
