#In this game the user has to guesss the number 
import random

def number(a,b):
    number = random.randint(a, b)
    return number

num1 = int(input("Enter the starting number of the range: "))
num2 = int(input("Enter the ending range for the number: "))

def game():
    num = number(num1, num2)
    user_input = int(input(f"Enter a number between {num1} and {num2}: "))
    while user_input != num:
        user_input = int(input(f"Enter a number between {num1} and {num2}: "))
        if user_input > num:
            print("The actual number is less than your guess.")
        elif user_input < num:
            print("The actual number is less than your guess.")
    
    print("Yay you have guessed it correctly!!!")

game()