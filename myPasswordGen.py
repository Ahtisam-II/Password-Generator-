import random
import string
def passGen (length):
    char = string.ascii_letters + string.digits 
    password = ''.join(random.choice(char) for _ in range(length))
    return password
again = True
print("Welcome  to password genrator program.")
while(again):
    try :
        length = int (input("Enter the length of Password: "))
        if length <= 0 :
            raise ValueError
    except ValueError:
        print("Please Enter valid length. ")
    else:
        password= passGen(length)
        print ("Genrated password : " , password)
    userChoice = input("Enter 'yes' or y to genrate password again. ").strip().lower()
    if (userChoice == 'y' or userChoice == "yes"):
        again = True
    else:
        again = False
        print("Thanks for using this program.")
        
     

    