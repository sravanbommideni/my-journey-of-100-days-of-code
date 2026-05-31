MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(item):
    missing_items=[]
    for i in MENU[item]['ingredients']:
        if resources[i]<MENU[item]['ingredients'][i]:
            missing_items.append(i)
    return ", ".join(missing_items)

def process_coins(item):
    print(f"cost of the item is : {MENU[item]['cost']}")
    print("insert coins :")
    quarters=int(input("How many quarters :\n[type in number format e.g: 2,3,6...] >"))
    dimes = int(input("How many dimes :\n[type in number format e.g: 2,3,6...] >"))
    nickels = int(input("How many nickels :\n[type in number format e.g: 2,3,6...] >")) #0.05
    pennies = int(input("How many pennies :\n[type in number format e.g: 2,3,6...] >")) #0.01
    value_of_coins = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return value_of_coins

def check_transaction(user_input,actual_cost,gain):
    if user_input < actual_cost:
        print("sorry not enough money....money refunded")
        return False,0
    else:
        gain = gain + actual_cost
        change=user_input - actual_cost
        if user_input > actual_cost:
            print(f"here is the {change:.2f} change...")
        return True,gain

def make_coffee(ingredients,resource,item):
    for i in resource:
        resource[i]-=ingredients[i]
    return f"here is your {item}..enjoy"

def report():
    for i in resources:
        print(f"{i} : {resources[i]}")
    return f"money : {profit}"

profit=0
start_new=True
while start_new:
    user_choice=input("What would you like? (espresso/latte/cappuccino) :\n>")
    if user_choice=="off":
        start_new=False
    else:
        if user_choice=="report":
            print(report())
        elif user_choice in MENU :
            not_available_resources=is_resources_sufficient(user_choice)
            if not_available_resources=="":
                user_money=process_coins(user_choice)
                liist = check_transaction(user_money, MENU[user_choice]['cost'], profit)
                if liist[0]:
                    profit = liist[1]
                    print(make_coffee(MENU[user_choice]['ingredients'],resources,user_choice))
            else:
                print(f"sorry not enough {not_available_resources}")
