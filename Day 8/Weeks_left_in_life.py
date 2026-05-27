current_age=int(input("enter your current age : \n"))
def life_in_weeks(x):
    years_left=90-x
    weeks_left=years_left*52
    return weeks_left
print(f"You have {life_in_weeks(current_age)} weeks left")