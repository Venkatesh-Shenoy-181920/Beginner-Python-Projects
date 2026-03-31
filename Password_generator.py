import random

#The characters available for making the password
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'", ';', ':', 
              '"', '?', '[', ']', '{', '}', '/', '|', '<', '>', ',', '.', '!',
              '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+']

#The password maker function
def password_maker(length):
    password = '' #The empty string which will become our password
    for i in range(1, length + 1): #Loop to create the password
        character = random.choice(characters)
        password += character
    return password #The generated password is returned

#Welcome text
print("This is the password generator")
print("WELCOME")
print("Minimum length recommended is 12-16 characters")
length = int(input("Enter the length of the password you would like: ")) #Length of the password
password = password_maker(length) #The returned password
print(f"Your password is: {password}")
print("!!CAUTION: DO NOT SHARE THIS WITH ANYONE!!")