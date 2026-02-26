#we generate a module that creates a function to identify the random numbers
import random

print("WELCOME TO MY NUMBER GAME 😀")

#ask the player if they ant to play
player=input("Do you want to play? ")
if player.strip().lower()!= "yes":  #if the user says anything other than yes the code is terminated
    quit()

top_range=input("Type a number: ")      #we ask the user to type in a number range

#we make sure the number type in is an integer
if top_range.isdigit():
    top_range=int(top_range)    #if its an integer it is now converted here from a string t

    if top_range <= 0 :
        print("Please type a number larger than 0 next time.")     #here we make sure the number that the user types is in range
        quit()
else:
    print("Please type a number next time.")    #If the user doesnt type a number the code is terminated
    quit()

random_number =random.randint(0,top_range)   #this is where the random numbers are stored

guess=0
#here a loop is created until the user guesses correctly
while True:
    guess += 1  #here we keep truck of how many guesses the user got
    user_guess=input("Make your guess: ")
    if user_guess.isdigit():    #the again makes sure the input of the user is a number
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")    #if not a number the loop starts over again til a number is typed
        continue

    if user_guess==random_number:   #checks if the guess if the user matches the random number
        print("NICE YOU GOT IT😁")
        break                       #if it matches the loop breaks
    else:
        print("SORRY YOU DIDN'T GET IT😌")

print("You got it in",guess,"guesses.")


print(random_number)