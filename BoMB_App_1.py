########################## app to prototype BoM Baseball/learning game ##############################

#import [sys, json, random, time] modules
import sys
import json 
import random
import time

#(ref) get Book of Mormon JSON as bom1

json_file = open("C:\\Users\\loisj\\Documents\\GitHub\\scriptures-json\\reference\\book-of-mormon-reference-format.json")
bom1 = json.load(json_file)
json_file.close()

#create typing effect
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

#Welcome Message
delay_print("Hello young scholar!")
time.sleep(.100)
delay_print(" Let's start playing!\n")
time.sleep(.500)
input("press 'Enter' to continue:\n")

#create game function
def game():
    #Assign variables to random book, chapter, and verse
    sbook = random.choice(list(bom1.keys()))           
    schap = random.choice(list(bom1[sbook]))           
    sverse = random.choice(list(bom1[sbook][schap]))   
    #Initialize life system
    tries = 0
    
    delay_print("Alright! Here is your verse. Do you know where it is in the Book of Mormon?:\n\n" + "\"" + str(bom1[sbook][schap][sverse]) + "\"" + "\n")  #prints txt from random verse
    time.sleep(1.5)
    
    while True:
        delay_print("\nFirst guess the Book:")
        bookguess = input()
        if bookguess != sbook:
            tries = tries + 1
            delay_print("try again!")
        else:
            break

    delay_print("Great job!")
    time.sleep(.500)
    while True:

        delay_print("\nGuess the chapter in " + str(sbook) + ":")

        chguess = input()

        if chguess != schap:
            tries = tries + 1
            print("Try again!")
        else:
            break
        
    delay_print("\nHooray! You win! " + str(sbook) + " " + str(schap) + " is the correct answer!\n")
    delay_print("\nYou got the correct answer in: " + str(tries) + " tries!")
    time.sleep(.500)
    delay_print("\nWould you like to play again? (y/n):")
    ans = input()
    if ans == "y":
        game()
    elif ans == "n":
        delay_print("Thanks for playing!")

#Execute game function
game()

""" To Do:
        Life System
        Guess the Book and chapter immediately if you know it
        Use a Life to verify the book
        If you fail, provide learning context (i.e., 'Nice try! Remember [insert context based on keyword] and [etc]. The key stuff happening here is [].)
        Style
        GUI

    """        