#The source code for the main game

#importing all the hangman figures and list of words
from body import figure_1
from body import figure_2
from body import figure_3
from body import figure_4
from body import figure_5
from body import figure_6
from body import dead_figure
from words import words
import random

#The game function
def game():
    #To select the words
    word = random.choice(words).upper()
    letters = list(word)
    new_letters = tuple(letters) #Storing the letter in a tuple to make reference list
    lives = 6
    print(figure_1)
    print(f"You have {lives}, Good Luck!")

    while len(letters) != 0:
        num_letters = len(letters)
        print(f"\nThere are {num_letters} in the word.")
        print("_"*num_letters)
        letter = input("Enter the letter: ").upper()
        if letter in letters:
            letters.remove(letter)
            remaining_letters = [] #Creating and assigning the letters remaining to the new list
            remaining_letters = remaining_letters + letters
        else:
            lives -= 1
        
        #Displaying the figures
        if lives == 5:
            print('\n', figure_2)
            print(f"You have {lives} lives remaining.") 
        elif lives == 4:
            print('\n', figure_3)
            print(f"You have {lives} lives remaining.")
        elif lives == 3:
            print('\n', figure_4)
            print(f"You have {lives} lives remaining.")
        elif lives == 2:
            print('\n', figure_5)
            print(f"You have {lives} lives remaining.")
        elif lives == 1:
            print('\n', figure_6)
            print(f"You have {lives} lives remaining.")
        elif lives == 0:
            print('\n', dead_figure)
            print(word, ' was the letter la, It was soo simple la,')
            print("You couldn't even get that right, Are you stoobid")
            print("Why can't you be like Timmy la, he knows 111100000 words. He is 5")
            break
    
    #User won the game.
    if lives > 0:  
        if list(new_letters) == remaining_letters:
            print(word, 'is the word.')
            print("I bet you are Timmy la.")
    else:
        print("You must be Timmy la") 
            
    print("Created by S Venkatesh Shenoy")
    print("For any suggestions please sent it to the email address: v66201200@gmail.com")

    
game()

#Asking user to play again
user_input = True
while user_input == True:
    play_again = input("Do you want to play again Yes/No: ").capitalize()
    if play_again == 'Yes':
        game()
    else:
        user_input = False
        print("Have a nice day")
        