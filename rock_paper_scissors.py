import random

user_wins=0     #the users score
comp_wins=0     #the computers score

options=["rock", "paper", "scissors"]       #the items used in the options

while True:
    user_input=input("Type Rock/Paper/Scissors or 'Q' if you want to quit:  ").strip().lower()   #ask the user to type in either rock paper or scissors

    if user_input== "q":        #if the user types q the program ends here
        print("Goodbye.")
        break

    if user_input not in options:       #The loop will not break until the user inputs the required string
        continue

    random_number=random.randint(0,2)     #the numbers here represent the stings inside the game list
                                                 #rock 0,paper 1,scissors 2
    comp_picked=options[random_number]   #tell us what the computer picked
    print(f"Computer picked {comp_picked}.")

    if user_input== "rock" and comp_picked == "scissors":
        print("YOU WON")
        user_wins += 1
        continue

    if user_input == "paper" and comp_picked == "rock":
        print("YOU WON")
        user_wins += 1
        continue

    if user_input == "scissors" and comp_picked == "paper":
        print("YOU WON!")
        user_wins +=1
        continue


    else:
        print("YOU LOST!")
        comp_wins += 1


print("You won",user_wins,"times ")
print("Computer won" ,comp_wins,"times")
