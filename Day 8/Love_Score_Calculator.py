def calculate_love_score(name1,name2):
    true_score = 0
    love_score = 0
    for letter in name1:
        if letter=="t" or letter=="r" or letter=="u" or letter=="e":
            true_score+=1
        if letter=="l" or letter=="o" or letter=="v" or letter=="e":
            love_score+=1
    for letter in name2:
        if letter=="t" or letter=="r" or letter=="u" or letter=="e":
            true_score+=1
        if letter=="l" or letter=="o" or letter=="v" or letter=="e":
            love_score+=1
    return f"love score is : {true_score}{love_score}"

name_1=input("enter first name :\n>")
name_2=input("enter second name :\n>")
print(calculate_love_score(name_1,name_2))