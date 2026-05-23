import random
import sys
list=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    start = input("do u want to play blackjack ?\n")
    user_cards = []
    computer_cards = []
    if start == "yes":
        user_cards.extend(random.choices(list, k=2))
        computer_cards.extend(random.choices(list, k=2))
    print(f"your cards are {user_cards} and computer card is {computer_cards[0]}")
    sum_of_user_cards = 0
    sum_of_computer_cards = 0
    for card in user_cards:
        sum_of_user_cards += card
    for card in computer_cards:
        sum_of_computer_cards += card
    if sum_of_user_cards > 21:
        user_cards.remove(11)
        user_cards.append(1)
    stand = False
    while not stand:
        hit_or_stand = input("do u want to \'hit\' or \'stand\' ?\n")
        if hit_or_stand == "stand":
            while sum_of_computer_cards < 17:
                new_card = random.choice(list)
                computer_cards.append(new_card)
                sum_of_computer_cards += new_card
            print(f"user cards are {user_cards}")
            print(f"computers cards are {computer_cards}")
            print(f"sum of your cards :{sum_of_user_cards} and sum of computer cards :{sum_of_computer_cards}")
            if sum_of_computer_cards > 21:
                print("you won....")
                stand = True
                blackjack()
            elif sum_of_computer_cards > sum_of_user_cards:
                print("you lost...")
                stand = True
                blackjack()
            elif sum_of_computer_cards<sum_of_user_cards:
                print("you lost...")
                stand = True
                blackjack()
            else:
                print("draw..")
                stand = True
                blackjack()
        else:
            new_card = random.choice(list)
            user_cards.append(new_card)
            sum_of_user_cards += new_card
            print(f"user cards are {user_cards}")
            if sum_of_user_cards > 21:
                print("you lost")
                stand = True
                blackjack()
blackjack()
