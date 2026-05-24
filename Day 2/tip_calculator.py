print("Welcome to the tip calculator....\n")
bill=float(input("how much was your bill? : "))
tip=int(input("how much percentage of tip would u like to give? 10,12,15? : "))
if tip==10 :
    total_bill = 1.10 * bill
elif tip==12 :
    total_bill = 1.12 * bill
elif tip==15 :
    total_bill = 1.15 * bill
num_of_frnds=int(input("how many people to split the bill? :"))
print(f"each person should pay : {round(total_bill/num_of_frnds,2)}")
