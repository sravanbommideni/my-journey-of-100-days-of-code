import random
import sys
user_cards=[]
computer_cards=[]
cards_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def deal_cards():
    """deals cards and returns the dealt cards"""
    user_cards.clear()
    computer_cards.clear()
    user_cards.extend(random.choices(cards_list,k=2))
    computer_cards.extend(random.choices(cards_list, k=2))
    sum_of_user_cards=sum(user_cards)
    if sum_of_user_cards>21:
        user_cards.remove(11)
        user_cards.append(1)
    if sum_of_user_cards==21:
        print("you won.....your cards sum is blackjack.....")
        print(f"your cards are {user_cards} and computer cards are {computer_cards}")
    return f"your cards are {user_cards} and computer card is {computer_cards[0]}"

def start():
    play = input("do u want to play blackjack ?\n")
    if play=="yes":
        print(deal_cards())
    elif play=="no":
        sys.exit()
    else:
        while play not in ["yes","no"]:
            play = input("enter valid input ?\n")
            print(deal_cards())

def add_cards_if_comp_sum_less_than_17(list2):
    while sum(list2) < 17:
        new_card = random.choice(cards_list)
        list2.append(new_card)

def compare(l1,l2):
    sum_of_computer_cards=sum(l2)
    sum_of_user_cards=sum(l1)
    if sum_of_computer_cards>21:
        print("You won....computer cards sum exceeded blackjack")
        return 0
    elif sum_of_user_cards>sum_of_computer_cards:
        print(f"you won...your cards sum is {sum_of_user_cards} and computer cards sum is {sum_of_computer_cards}")
        return 0
    elif sum_of_user_cards<sum_of_computer_cards:
        print(f"you lost...your cards sum is {sum_of_user_cards} and computer cards sum is {sum_of_computer_cards}")
        return 0
    else :
        print(f"DRAW MATCH...your cards sum is {sum_of_user_cards} and computer cards sum is {sum_of_computer_cards}")
        return 0

def stand(list1,list2):
    new_card=0
    add_cards_if_comp_sum_less_than_17(list2)
    sum_of_computer_cards=sum(list2)
    if new_card==11:
        if sum_of_computer_cards>21:
            list2.remove(11)
            list2.append(1)
            add_cards_if_comp_sum_less_than_17(list2)
    print(f"your cards are {user_cards} and computer cards are {computer_cards}")
    return compare(list1,list2)

def hit(liist):
    """called when user picks up another card"""
    sum_of_user_cards=sum(liist)
    new_card = random.choice(cards_list)
    liist.append(new_card)
    sum_of_user_cards += new_card
    print(f"user cards are {liist}")
    if sum_of_user_cards > 21:
        print("you lost....your cards sum exceeded blackjack")
        return 0
    return None

def blackjack_fun():
    game_over = False
    start()
    while not game_over:
        hit_or_stand = input("do u want to \'hit\' or \'stand\' :\n")
        if hit_or_stand == "hit":
            x = hit(user_cards)
            if x == 0:
                game_over = True
                blackjack_fun()
        else:
            y = stand(user_cards, computer_cards)
            if y == 0:
                game_over = True
                blackjack_fun()
blackjack_fun()
