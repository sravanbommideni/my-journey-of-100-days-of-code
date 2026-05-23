import random
print("Welcome to the Password Generator!!!")
nr_letters=int(input("how many letters would u like?\n"))
Alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=["!","@","#","$","%","^","&","*","(",")","-","_","=","+","?","/",",",".","<",">",";","'","`","~"]
nr_symbols=int(input("How many symbols would u like?\n"))
nr_numbers=int(input("How many numbers would u like?\n"))
password=""
for char in range(nr_letters):
    password+=random.choice(Alphabets)
for symb in range(nr_symbols):
    password+=random.choice(symbols)
for num in range(nr_numbers):
    password+=random.choice(numbers)
password_list=[]
for i in password :
    password_list.append(i)
print(password_list)
random.shuffle(password_list)
print(password_list)
