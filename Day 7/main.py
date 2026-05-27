import random
from hangman_words import word_list,phase,welcome,logo
print(welcome)
print(logo)
word=random.choice(word_list)
word_length=len(word)
blank=""
for i in range(word_length):
    blank+="_"
print(blank)
lives=0
print("you have 6 lives")
game_over=False
guessed=[]
corrected_guess=[]
no_of_attempts_left=6

while not game_over:
    display=""
    guess=input("guess a letter:\n")
    if guess in [1,2,3,4,5,6,7,8,9,0]:
        print("you cant enter a number...enter a digit instead.")
        guess=input()
    if guess in guessed:
        print("you have already guessed this number...choose another")
        guess = input()
    guessed.append(guess)
    #if guess is wrong , cut the life.
    if guess not in word:
        lives+=1
        no_of_attempts_left-=1
        if no_of_attempts_left!=0:
            print(f"you have got {no_of_attempts_left} lives left....")
        if lives == 6:
            game_over = True
            print("**********YOU LOST**********")
    #for displaying to user.
    for letter in word:
        if letter==guess:
            display+=letter
            corrected_guess.append(guess)
        elif letter in corrected_guess:
            display+=letter
        else:
            display+="_"
    print(display)
    #condition for completing the guessing correctly
    if "_" not in display:
        game_over=True
        print("**********YOU WON**********")
    print(phase[lives])
