import sys
print("Welcome to the treasure island!!\nYour mission is to find the treasure.\nYou have three steps to reach the treasure.")
print("STEP 1 :")
direction=input("You are at a chowrasta , Which direction do u want to go to find the treasure?\n\ttype \"left\" or \"right\" or \"up\" or \"down\" : \n" ).replace(" ",'').lower()
if direction!="left":
    print('Oops...you fell into a hole.\nGAME OVER!!!!')
    sys.exit()
else :
    print("you've come to a lake. There is an island in the middle of the lake.")
    swim_wait=input("\ttype \"wait\" to wait for a boat. type \"swin\" to swim across: \n").replace(" ", "").lower()
    if swim_wait!="wait" :
        print('you are ATTACKED by a trout.\nGAME OVER!!!!')
        sys.exit()
    else :
        print("you have arrived at the island unharmed. there is a house with 4 doors here...")
        door=input("\tone red, one green , one blue and an yellow\n").replace(" ", "").lower()
        if door=='red' :
            print('you are BURNED by fire.\nGAME OVER!!!!')
        elif door in ['blue','Blue'] :
            print('you are EATEN by beasts.\nGAME OVER!!!!')
        elif door!='yellow' :
            print('you are beaten at last step.\nGAME OVER!!!!')
        else :
            print('YOU WIN!!!!')
