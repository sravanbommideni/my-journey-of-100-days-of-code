import random

account_b=random.choice(data)
game_should_continue=True
score=0

#formatting the data into printable format
def formatting_data(dict):
    account_name=dict["name"]
    account_description=dict["description"]
    account_country=dict["country"]
    return f"{account_name} , a {account_description} , from {account_country}"

def check(user_guess,acc_1_followers,acc2_followers):
    if acc_1_followers>acc2_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"

while game_should_continue:
    #generating random accounts from data
    account_a=account_b
    account_b = random.choice(data)

    while account_a==account_b:
        account_b=random.choice(data)

    print(f"compare A : {formatting_data(account_a)}")
    print("V/S")
    print(f"account B : {formatting_data(account_b)}")

    #taking user input
    guess=input("who has more followers ? \'A\' or \'B\'").lower()
    print("\n"*30)

    #calculate account a and b followers
    account_a_followers=account_a["follower_count"]
    account_b_followers=account_b["follower_count"]

    yes_or_no=check(guess,account_a_followers,account_b_followers)

    if yes_or_no==True:
        score+=1
        print(f"your current score is {score}")
    else:
        print("you have guessed it wrong...")
        print(f"final score is {score}")
        game_should_continue=False
