import random
game_over=False
num=random.randint(1,100)
user={
    'guesses_left':0,
    'difficulty':"",
    'target':num,
    'guessed':[]
}
def check(n):
    if n==user['target']:
        print(f"you got it...the answer was {num}")
        return True
    elif n<user['target']:
        user["guesses_left"]-=1
        print("too low")
        print(f"guesses left : {user["guesses_left"]}")
        return False
    else :
        user["guesses_left"] -= 1
        print("too high")
        print(f"guesses left : {user["guesses_left"]}")
        return False

print("Welcome to number guessing game....\nI have guessed a number from between 1 and 100")
print("choose your difficulty : \'easy\' or \'hard\'")
while user["difficulty"] not in ["easy","hard"]:
    user["difficulty"]=input(">")
    if user["difficulty"]=="easy":
        user["guesses_left"]=10
        print(f"guesses left : {user["guesses_left"]}")
    elif user["difficulty"]=="hard":
        user["guesses_left"] = 5
        print(f"guesses left : {user["guesses_left"]}")

while not game_over:
    if user["guesses_left"] != 0:
        print("guess a number")
        guess=int(input(">"))
        while guess in user['guessed']:
            print("you have already guessed this number , choose another...")
            guess = int(input(">"))
        user['guessed'].append(guess)
        game_over=check(guess)
    else:
        print("you have used all your chances....")
        game_over=True
