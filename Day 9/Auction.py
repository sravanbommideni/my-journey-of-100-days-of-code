dict={}
over=False
while not over:
    name=input("Enter your name :\n")
    bid=int(input("how much are u bidding? :\n"))
    dict[name]=bid
    no_exit=input("is anyone else bidding? :\n").lower()
    if no_exit=="no":
        over=True
    elif no_exit=="yes":
        print("\n"*20)
    else:
        while no_exit not in ["yes","no"]:
            print("enter valid input :\n")

winner=max(dict,key=dict.get) #to get key with highest value

highest_bid=max(dict.values()) #to get highest value

print(f"the person with highest bid is \"{winner}\" making a bid of \'{highest_bid}$\'....")
