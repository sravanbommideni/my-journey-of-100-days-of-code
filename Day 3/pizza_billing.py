import sys
print("""Welcome to python pizza deliveries.""")
print("what size of pizza do u want? :")
size=input("""\ttype \'L\' for large , \'M\' for medium and \'S\' for small.\n""").replace(" ","").lower()
print("do u want to add pepperoni on your pizza? :")
pepperoni=input("""\ttype \'Y\' for a yes , \'N\' for a no\n""").replace(" ","").lower()
print("do u want extra cheese? :")
extra_cheese=input("""\ttype \'Y\' for a yes , \'N\' for a no\n""").replace(" ","").lower()
if size=="s":
    bill=15
    if pepperoni=="y":
        bill+=2
    if extra_cheese=="y":
        bill+=1
elif size=="m":
    bill=20
    if pepperoni=="y":
        bill+=3
    if extra_cheese=="y":
        bill+=1
elif size=="l":
    bill=25
    if pepperoni=="y":
        bill+=3
    if extra_cheese=="y":
        bill+=1
else :
    print("enter valid size...")
    sys.exit()
print(f"your final bill is :{bill}")