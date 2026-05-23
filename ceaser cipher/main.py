def ceaser(message,shift,user_choice):
    result = ""
    for i in message:
        if user_choice=="encode":
            if i in alphabets:
                required = (alphabets.index(i) + shift) % 26
                result += alphabets[required]
            elif i in ALPHABETS:
                required = (ALPHABETS.index(i) + shift) % 26
                result += ALPHABETS[required]
            else:
                result += i
        else:
            if i in alphabets:
                required = (alphabets.index(i) - shift) % 26
                result += alphabets[required]
            elif i in ALPHABETS:
                required = (ALPHABETS.index(i) - shift) % 26
                result += ALPHABETS[required]
            else:
                result += i
    print(f"your {user_choice}d text : {result}")
ALPHABETS=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
over=False
while not over:
    user_choice=input("type \'decode\' to decrypt or type \'encode\' to encrypt :\n").lower()
    while user_choice not in ["encode","decode"]:
        user_choice=input("enter valid input(encode or decode) :\n")
    msg=input("type your message :\n")
    shift_number=int(input("enter the shift number:\n"))
    ceaser(message=msg,shift=shift_number,user_choice=user_choice)
    exit_flag=input("types \'yes\' to continue or type \'no\' to discontinue...\n").lower()
    while exit_flag not in ["yes","no"]:
        exit_flag=input("invalid input\ntypes \'yes\' to continue or type \'no\' to discontinue...\n").lower()
    if exit_flag=="no":
        over=True
